#ifndef GET_KHOP_BENCHMARK_H    // To make sure you don't declare the function more than once by including the header multiple times.
#define GET_KHOP_BENCHMARK_H

#include "orderings.h"
#include <chrono>
#include <numeric>

using namespace std;


class GetKHopBenchmark
{
    public:
        vector<Vertex> getNeighboursVector(Vertex *, Graph *);
        Graph readGraph();
        vector<int> calcOrder(string);
        double runBenchmark();
        void runExperiment();
        void displayStats();
        void calcStats();
        void printVertexOrder();
        GetKHopBenchmark(int, string, int, string, int); 

        size_t nNodes;
        string path;
        string order; 
        int nExpts;
        int K;
        double mean;
        double stdev;
        map<int, vector<Vertex>> khopNeighbours;
        map<string, double> stats;
        vector<pair<Vertex, Vertex>> edges{};
        vector<int> vertexOrder;
        vector<double> execTimes;
        Graph graph;
};

#endif