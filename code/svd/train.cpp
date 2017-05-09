#include <vector>
#include <iostream>
#include "svd.hpp"
#include "parse.hpp"

int main() {
    std::cout << "Loading data" << std::endl;
    std::vector<triplet> points;
    sp_mat A = parse::data_sp_mat(points);

    mat U, V;
    PMF pmf(A, U, V, points, 50);
    pmf.predict("../../data/um/qual.dta", "pmf-prediction.dta");
}

