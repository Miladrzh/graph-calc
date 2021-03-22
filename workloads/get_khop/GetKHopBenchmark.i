/* example.i */
%include "std_string.i"
%include "std_set.i"
%include "std_vector.i"
%module GetKHopBenchmark 
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
}
%{
    /* Put header files here or function declarations like below */
    #include "orderings.h"
    #include "GetKHopBenchmark.h"
    #include <chrono>
    #include <numeric>
    using namespace std;
    using namespace boost;
    using Graph = compressed_sparse_row_graph<>;
    using Vertex = Graph::vertex_descriptor;
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
%}

%include "orderings.h"
%include "GetKHopBenchmark.h"


// template <typename A, typename B>
// std::pair<B, A> flip_pair(const std::pair<A, B> &);
// template <typename A, typename B>
// std::multimap<B, A> flip_map(const std::map<A, B> &);
// extern std::map<int, int> getDegrees(Graph *);
// extern std::vector<int> degOrdDesc(Graph *);
// extern std::vector<int> randomOrd(int);
// extern std::map<int, int> degreeDistribution(Graph *);