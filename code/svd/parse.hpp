#ifndef _PARSE_HPP_
#define _PARSE_HPP_

#include <Eigen/Sparse>
#include <fstream>
#include <vector>

namespace parse {

typedef Eigen::Triplet<double> triplet;
typedef Eigen::SparseMatrix<double> sp_mat;

void fill_data_vector(std::vector<triplet> &values) {
    std::ifstream file("../../data/um/training.dta");
    int uid, mid, rating;
    while (file >> uid >> mid >> rating) {
        values.push_back(triplet(uid, mid, rating));
    }
}

sp_mat data_sp_mat(std::vector<triplet> &values) {
    sp_mat matrix(458294, 17771);
    fill_data_vector(values);
    matrix.setFromTriplets(values.begin(), values.end());
    return matrix;
}

} // namespace parse

namespace terminal {

void clear_line() {
    std::cout << "\33[2K\r" << std::flush;
}

} // namespace terminal

#endif // _PARSE_HPP_
