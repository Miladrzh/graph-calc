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
        vector<int> getAllSinkIds();
        vector<pair<int, int>> getVectorWeights();
        vector<double> getExecTimes();
        vector<int> getVsSeen();

        Graph readGraph();

        void printAllSinkIds();
        void printVertexOrder();
        void displayStats();
        vector<int> buildCumSum();
        vector<int> calcOrder(string);
        void calcAllSinkIds();
        void calcStats();
        pair<double, int> runBenchmark();
        void runExperiment();
        int sample();

        GetKHopBenchmark(size_t, string, int, string, int, int); 

        size_t nNodes;
        int nSinks;
        int nIncomps; // number of times a khop query did not complete k hops
        int nSeenAll; // number of times a khop query returned all the vertices in the graph
        string path;
        string order; 
        int nExpts;
        int K;
        int nSamples;
        double mean;
        double stdev;
        map<int, vector<Vertex>> khopNeighbours;
        map<string, double> stats;
        vector<pair<Vertex, Vertex>> edges{};
        vector<int> vertexOrder;
        set<int> sids; // node ids for Sink nodes
        vector<double> execTimes; // execution time per experiment
        vector<int> vsSeen; // number of vs seen per experiment
        Graph graph;
        vector<pair<int, int>> sortedWts;
        vector<int> cumSumWts;
};

#endif