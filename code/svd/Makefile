all: svd

svd.o: svd.cpp
	g++ -std=c++11 -Wall -Ofast -c svd.cpp -o bin/svd.o

parse.o: parse.cpp
	g++ -Wall -Ofast -c parse.cpp -o bin/parse.o

svd: svd.o parse.o
	g++ -std=c++11 -Wall -Ofast bin/* train.cpp -o svd

clean:
	rm -f svd bin/*.o
