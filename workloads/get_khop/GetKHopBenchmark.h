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
        vector<int> getAllSinkIds();
        void calcAllSinkIds();
        void printAllSinkIds();
        double runBenchmark();
        void runExperiment();
        void displayStats();
        void calcStats();
        void printVertexOrder();
        
        GetKHopBenchmark(size_t, string, int, string, int); 

        size_t nNodes;
        int nSinks;
        int nIncomps; // number of times a khop query did not complete k hops
        int nSeenAll; // number of times a khop query returned all the vertices in the graph
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
        set<int> sids; // node ids for Sink nodes
        vector<double> execTimes;
        Graph graph;
};

#endif