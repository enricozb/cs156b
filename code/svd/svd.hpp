#ifndef _SVD_HPP_
#define _SVD_HPP_

#include <Eigen/Sparse>
#include <vector>
#include <iostream>
#include <string>
#include <math.h>
#include <random>
#include <map>
#include "parse.hpp"
#include "datum.hpp"

#define NUM_MOVIES 17770
#define NUM_USERS 458293
#define NUM_DAYS 2243

#define NUM_BINS 30

using namespace Eigen;

typedef Eigen::SparseMatrix<double> sp_mat;
typedef Eigen::Matrix<double, Dynamic, Dynamic, RowMajor> mat;
typedef Eigen::Triplet<double> triplet;

class SVD {
  protected:
    sp_mat &A;                      // Dataset as a sparse matrix
    mat &U, &V;                     // Factor matrices
    double lambda;
    double lrate;
    int K;                          // Number of latent factors
    std::vector<triplet> &points;   // Dataset as triplets

    double mu = 0;  // average rating
    mat Ub;         // user biases
    mat Vb;         // movie biases

  public:
    SVD(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K);

    virtual double predict(int uid, int mid);
    void predict(std::string infile_s, std::string outfile_s);

    void train(int iterations);
    void save(int curr_iter);
};

class PMF : public SVD {
    std::default_random_engine generator;
    double noise = sqrt(0.5);
    std::normal_distribution<double> distribution;

  public:
    PMF(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K);

    double predict(int uid, int mid) override;
    using SVD::predict;
};

class TimeSVDpp: public SVD {
    // we'll just 1-index these vv don't hate me
    // initing all to 0, will be properly calculated in beginning of train()
    double user_bias[NUM_USERS + 1] = {0};
    double movie_bias[NUM_MOVIES + 1] = {0};
    double alpha[NUM_USERS + 1] = {0};
    int mean_rating_date[NUM_USERS + 1] = {0};
    int total_ratings_for_user[NUM_USERS + 1] = {0};

    int total_ratings_for_movie[NUM_MOVIES + 1] = {0};


    std::vector<datum> &data; 

  public: 
    TimeSVDpp(sp_mat &A, mat &U, mat &V, std::vector<triplet> &points, int K,
            std::vector<datum> &data);

    void train(int iterations);
    double predict(int uid, int mid, int time);
    void predict(std::string infile_s, std::string outfile_s);

  private:
    double dev(int uid, int time); // time deviation
};

#endif // _SVD_HPP_
