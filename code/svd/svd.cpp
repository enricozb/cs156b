#include <Eigen/Sparse>
#include <vector>
#include <iostream>
#include <string>
#include <math.h>
#include "parse.hpp"

using namespace Eigen;

typedef Eigen::SparseMatrix<double> sp_mat;
typedef Eigen::Matrix<double, Dynamic, Dynamic, RowMajor> mat;
typedef Eigen::Triplet<double> triplet;

class SVD {
    sp_mat &A;                      // Dataset as a sparse matrix
    mat &U, &V;                     // Factor matrices
    double lambda;
    double lrate;
    int K;                          // Number of latent factors
    std::vector<triplet> &points;   // Dataset as triplets

    double mu = 0;  // average rating
    mat Ub;     // user biases
    mat Vb;     // movie biases

  public:
    SVD(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K) :
        A(A), U(U), V(V), K(K), points(points) {

        U = MatrixXd::Constant(A.rows(), K, 0.1);
        V = MatrixXd::Constant(A.cols(), K, 0.1);

        mu = A.sum() / points.size();
        A.makeCompressed();

        std::cout << "Shifting by average" << std::endl;
        A.coeffs() -= mu;

        lrate = 0.001;
        lambda = 0.05;
        this->train(10000);
    };

    double predict(int uid, int mid);
    void train(int iterations);
    void predict(std::string infile_s, std::string outfile_s);
};

double SVD::predict(int uid, int mid) {
    return mu + U.row(uid).dot(V.row(mid));
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

        if (i % 500 == 0) {
            std::ostringstream oss;
            oss << "predictions/prediction-K" << K << "-" << i << ".dat";

            const std::string filename = oss.str();
            this->predict("../../data/um/qual.dta", filename);
        }
    }
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

int main() {
    std::cout << "Loading data" << std::endl;
    std::vector<triplet> points;
    sp_mat A = parse::data_sp_mat(points);

    mat U, V;
    SVD svd(A, U, V, points, 100);
    svd.predict("../../data/um/qual.dta", "prediction-10.dta");
}
