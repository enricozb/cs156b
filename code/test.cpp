// Compile this file with g++ test.cpp -o test -std=c++11 -larmadillo -lmlpack
// to test if installation went OK

#include <mlpack/core.hpp>

using namespace mlpack;

int main() {
    arma::mat data;
    data::Load("data.csv", data, true);
    arma::mat cov = data * trans(data) / data.n_cols;
    data::Save("cov.csv", cov, true);
}