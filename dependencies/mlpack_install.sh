#!/bin/bash

# This should attempt to install armadillo + boost + cmake + mlpack

# ensure /usr/lib/include is searched
xcode-select install

# install armadillo
curl -L "https://sourceforge.net/projects/arma/files/armadillo-7.800.2.tar.xz" > "armadillo-7.800.2.tar.xz"
tar zxvf armadillo-7.800.2.tar.xz
cd armadillo-7.800.2
./configure
make
make install

# install boost 1.60
cd ..
curl -L "https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz/download" > "boost_1_63_0.tar.gz"
tar zxvf boost_1_63_0.tar.gz
cd boost_1_63_0
sudo ./bootstrap.sh --prefix=/usr/local
./b2 cxxflags="-stdlib=libc++"
sudo ./b2 install --prefix=/usr/local
cd ..

export $BOOST_ROOT /usr/local/boost

# install cmake
curl -O "https://cmake.org/files/v3.8/cmake-3.8.0.tar.gz"
tar -xf cmake-3.8.0.tar.gz
cd cmake-3.8.0
./bootstrap
make
make install
cd..

# install mlpack
git clone https://github.com/mlpack/mlpack
cd mlpack
mkdir build
cd build
cmake ..
make
make install
bin/mlpack_test
cd ..

