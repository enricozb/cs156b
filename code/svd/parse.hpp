#ifndef _PARSE_HPP_
#define _PARSE_HPP_

#include <Eigen/Sparse>
#include <vector>

namespace parse {

typedef Eigen::Triplet<double> triplet;
typedef Eigen::SparseMatrix<double> sp_mat;

void fill_data_vector(std::vector<triplet> &values);

sp_mat data_sp_mat(std::vector<triplet> &values);

} // namespace parse

namespace terminal {

void clear_line();

} // namespace terminal

#endif // _PARSE_HPP_
