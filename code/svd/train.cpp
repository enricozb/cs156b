#include <vector>
#include <iostream>
#include "svd.hpp"
#include "parse.hpp"

void svd() {
    std::cout << "Loading data" << std::endl;
    std::vector<triplet> points;
    sp_mat A = parse::data_sp_mat(points);

    mat U, V;
    // SVD svd = ___;
}

void pmf() {
    std::cout << "Loading data" << std::endl;
    std::vector<triplet> points;
    sp_mat A = parse::data_sp_mat(points);

    mat U, V;
    PMF pmf(A, U, V, points, 50);
    pmf.predict("../../data/um/qual.dta", "pmf-prediction.dta");  
}

void timesvdpp() {
    std::cout << "Loading data" << std::endl;
    std::vector<triplet> points;
    std::vector<datum> data;
    sp_mat A = parse::data_sp_mat(points);
    parse::fill_data_vector(data);

    mat U, V;
    TimeSVDpp tsp(A, U, V, points, 50, data);
    tsp.train(1000);
}

int main() {
    //svd();
    //pmf();
    timesvdpp();
}

