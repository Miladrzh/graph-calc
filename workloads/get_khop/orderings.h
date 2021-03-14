#ifndef ORDERINGS_H    // To make sure you don't declare the function more than once by including the header multiple times.
#define ORDERINGS_H

#include <boost/graph/compressed_sparse_row_graph.hpp>
#include <boost/range/iterator_range.hpp>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iostream>
#include <map>
#include <algorithm>    // std::random_shuffle
#include <vector>       // std::vector
#include <ctime>        // std::time
#include <cstdlib>      // std::rand, std::srand

using Graph = boost::compressed_sparse_row_graph<>;
using Vertex = Graph::vertex_descriptor;

template <typename A, typename B> std::pair<B, A> flip_pair(const std::pair<A, B> &);
template <typename A, typename B> std::multimap<B, A> flip_map(const std::map<A, B> &);
std::map<int, int> getDegrees(Graph *);
std::vector<int> degOrdDesc(Graph *);
std::vector<int> randomOrd(int);
std::map<int, int> degreeDistribution(Graph *);

#endif