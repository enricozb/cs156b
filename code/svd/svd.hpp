#ifndef _SVD_HPP_
#define _SVD_HPP_

#include <Eigen/Sparse>
#include <vector>
#include <iostream>
#include <string>
#include <math.h>
#include <random>
#include "parse.hpp"

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

#endif // _SVD_HPP_
