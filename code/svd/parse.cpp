#include <Eigen/Sparse>
#include <fstream>
#include <vector>
#include <iostream>
#include "parse.hpp"

namespace parse {

typedef Eigen::Triplet<double> triplet;
typedef Eigen::SparseMatrix<double> sp_mat;

struct datum {
    int uid;
    int mid;
    int date;
    int rating;
};

void fill_data_vector(std::vector<triplet> &values) {
    std::ifstream file("../../data/um/training.dta");
    int uid, mid, rating;
    while (file >> uid >> mid >> rating) {
        values.push_back(triplet(uid, mid, rating));
    }
}

// version of points with dates included
void fill_data_vector(std::vector<struct datum> &values) {
    std::ifstream file("../../data/um/training_with_dates.dta");
    int uid, mid, rating, date;
    while (file >> uid >> mid >> date >> rating) {
        struct datum d;
        d.uid = uid;
        d.mid = mid;
        d.date = date;
        d.rating = rating;
        values.push_back(d);
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

