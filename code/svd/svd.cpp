#include <Eigen/Sparse>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <random>
#include "parse.hpp"
#include "svd.hpp"

using namespace Eigen;

typedef Eigen::SparseMatrix<double> sp_mat;
typedef Eigen::Matrix<double, Dynamic, Dynamic, RowMajor> mat;
typedef Eigen::Triplet<double> triplet;

SVD::SVD(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K) :
    A(A), U(U), V(V), K(K), points(points) {

    U = MatrixXd::Constant(A.rows(), K, 0.1);
    V = MatrixXd::Constant(A.cols(), K, 0.1);

    mu = A.sum() / points.size();
    A.makeCompressed();

    std::cout << "Shifting by average" << std::endl;
    A.coeffs() -= mu;

    lrate = 0.001;
    lambda = 0.02;
    //this->train(1000);
};

PMF::PMF(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K) :
    SVD(A, U, V, points, K) {
    distribution = std::normal_distribution<double>(0.0, noise);
}

double SVD::predict(int uid, int mid) {
    return mu + U.row(uid).dot(V.row(mid));
}

double PMF::predict(int uid, int mid) {
    double raw = mu + U.row(uid).dot(V.row(mid));
    return distribution(generator) + raw;
}

void SVD::train(int iterations) {
    std::vector<triplet>::iterator it;

    std::cout << "Training " << K << " latent factors with " << iterations
              << " iterations" << std::endl << std::endl;

    double total_err = 0;
    for (int i = 1; i <= iterations; i++) {
        for (int f = 0; f < K; f++) {
            terminal::clear_line();
            std::cout << "Training feature " << f + 1 << ", rmse: "
                      << sqrt(total_err/points.size()) << std::flush;

            total_err = 0;
            for (it = points.begin(); it != points.end(); ++it) {
                int uid = (*it).row();
                int mid = (*it).col();

                double err = (*it).value() - this->predict(uid, mid);
                total_err += err * err;

                auto U_uid_f = U(uid, f);
                U(uid, f) += lrate * (err * V(mid, f) - lambda * U(uid, f));
                V(mid, f) += lrate * (err * U_uid_f   - lambda * V(mid, f));
            }
        }
        terminal::clear_line();
        std::cout << "Iteration " << i << ", rmse: "
                  << sqrt(total_err/points.size()) << std::endl;

        if (i % 100 == 0) {
            std::ostringstream oss;
            oss << "predictions/pmf-qual-K" << K << "-I" << i << ".dat";
            this->predict("../../data/um/qual.dta", oss.str());

            oss.str("");
            oss << "predictions/pmf-probe-K" << K << "-I" << i << ".dat";
            this->predict("../../data/um/probe.dta", oss.str());

            this->save(i);
        }
    }
}

void SVD::save(int curr_iter) {
    std::cout << "Saving matrices to" << std::endl;
    std::ostringstream oss;
    oss << "predictions/pmf-U-K" << K << "-I" << curr_iter << ".mat";
    std::ofstream u_file(oss.str());

    oss.str("");
    oss << "predictions/pmf-V-K" << K << "-I" << curr_iter << ".mat";
    std::ofstream v_file(oss.str());

    u_file << U << std::endl;
    v_file << V << std::endl;
}

void SVD::predict(const std::string infile_s, const std::string outfile_s) {
    std::cout << "Predicting to: " << outfile_s << std::endl;
    std::ifstream infile(infile_s);
    std::ofstream outfile(outfile_s);

    outfile.setf(std::ios_base::fixed, std::ios_base::floatfield);
    outfile.precision(2);

    int uid, mid, date;
    while (infile >> uid >> mid >> date) {
        outfile << this->predict(uid, mid) << std::endl;
    }
}


// TimeSVD++
// Doing linear modelling of user biases as described in https://pdfs.semanticscholar.org/8451/c2812a1476d3e13f2a509139322cc0adb1a2.pdf

// In order, the things that still need to be implemented: 
// TODO add in time element for movie bias
// TODO do linear+ (add single-day effect)
// TODO add the ++ part of TimeSVD++

 TimeSVDpp::TimeSVDpp(sp_mat &A, mat &U, mat &V, 
            std::vector<triplet> &points, int K,
            std::vector<datum> &data) : SVD(A, U, V, points, K), data(data) {
    // points is never used in training once U and V are created
    // so we should toss it? TODO

    std::cout << "Initializing..." << std::endl;
    // Go through entire dataset to calculate:
    // - total_ratings_for_user
    // - mean_rating_date
    // - user_bias
    // - movie_bias
    // - total_ratings_for_user
    auto it = data.begin();

    for (it = data.begin(); it != data.end(); it++) {
        int uid = it->uid;
        int mid = it->mid;
        int date = it->date;
        double rating = it->rating;

        total_ratings_for_user[uid] += 1;
        total_ratings_for_movie[mid] += 1;
        mean_rating_date[uid] += date; // int should be large enough...? 
        user_bias[uid] += rating - mu;
        movie_bias[mid] += (rating - mu) / total_ratings_for_movie[mid]; 
        // divide here to ward off overflow at risk of higher numerical inaccuracy?
    }
    // go through all users and divide appropriately
    for (int i = 1; i <= NUM_USERS; i++) {
        mean_rating_date[i] /= total_ratings_for_user[i];
        user_bias[i] /= total_ratings_for_user[i];
    }
 }

double TimeSVDpp::dev(int uid, int t) {
    int t_u = mean_rating_date[uid];
    double result = pow(abs(t - t_u), 0.4); 
    // 0.4 used in the paper, we can try messing with it TODO
    if (t < t_u) result *= -1;

    return result;
}

double TimeSVDpp::predict(int uid, int mid, int t) {
    // TODO
    // get time bin from time
    //int bin = time / NUM_BINS;
    double rating;

    // linear modelling of user biases
    rating = mu + user_bias[uid] 
             + alpha[uid] * dev(uid, t) 
             + movie_bias[mid]
             // TODO + movie time term
             + U.row(uid).dot(V.row(mid));
            // TODO add svd++ term

    return rating;
}

void TimeSVDpp::predict(const std::string infile_s, const std::string outfile_s) {
    std::cout << "Predicting to: " << outfile_s << std::endl;
    std::ifstream infile(infile_s);
    std::ofstream outfile(outfile_s);

    outfile.setf(std::ios_base::fixed, std::ios_base::floatfield);
    outfile.precision(2);

    int uid, mid, date;
    while (infile >> uid >> mid >> date) {
        outfile << this->predict(uid, mid, date) << std::endl;
    }
}

void TimeSVDpp::train(int iterations) {

    std::cout << "Training " << K << " latent factors with " << iterations
              << " iterations" << std::endl << std::endl;

    double total_err = 0;
    for (int i = 1; i <= iterations; i++) { 
        for (int f = 0; f < K; f++) {
            terminal::clear_line();
            std::cout << "Training feature " << f + 1 << ", rmse: "
                      << sqrt(total_err/points.size()) << std::flush;

            total_err = 0;
            auto it = data.begin();
            for (it = data.begin(); it != data.end(); ++it) {
                int uid = it->uid;
                int mid = it->mid;
                int date = it->date;
                double rating = it->rating;

                double err = rating - this->predict(uid, mid, date);
                total_err += err * err;

                auto U_uid_f = U(uid, f);
                U(uid, f) += lrate * (err * V(mid, f) - lambda * U(uid, f));
                V(mid, f) += lrate * (err * U_uid_f   - lambda * V(mid, f));
                alpha[uid] += lrate * (err * dev(uid, date) - lambda * alpha[uid]);
            }
        }
        terminal::clear_line();
        std::cout << "Iteration " << i << ", rmse: "
                  << sqrt(total_err/data.size()) << std::endl;

        if (i % 100 == 0) {
            std::ostringstream oss;
            oss << "predictions/pmf-qual-K" << K << "-I" << i << ".dat";
            this->predict("../../data/um/qual.dta", oss.str());

            oss.str("");
            oss << "predictions/pmf-probe-K" << K << "-I" << i << ".dat";
            this->predict("../../data/um/probe.dta", oss.str());

            this->save(i);
        }
    }


}



























