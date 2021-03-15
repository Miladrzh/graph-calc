#include "GetKHopBenchmark.h"
#include <boost/tokenizer.hpp>
#include <boost/algorithm/string.hpp>
using namespace std;
using namespace boost;
using Graph = compressed_sparse_row_graph<>;
using Vertex = Graph::vertex_descriptor;
using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;


// get a vertex's neighbours as a vector
vector<Vertex> GetKHopBenchmark::getNeighboursVector(Vertex *vertex, Graph *graph)
{
    vector<Vertex> vec = vector<Vertex>();
    for (auto [neighbor, end] = adjacent_vertices(*vertex, *graph); neighbor != end; ++neighbor)
        vec.push_back(*neighbor);
    return vec;
}

Graph GetKHopBenchmark::readGraph()
{
    size_t vertices = nNodes;
    vector<pair<Vertex, Vertex>> edges{};

    ifstream ifs(path);

    char_separator<char> sep(" , ");


    for (string s; getline(ifs, s);)
    {

        string delimiter = " , ";
        string start = s.substr(0, s.find(delimiter));

        s.erase(0, s.find(delimiter) + delimiter.length());

        int from = stoi(start);
        int to = stoi(s);
        
        edges.emplace_back(from, to);
    }

    Graph graph{edges_are_sorted, edges.begin(), edges.end(), vertices};
    return graph;
}

vector<int> GetKHopBenchmark::calcOrder(string order)
{
    vector<int> vs = vector<int>{};
    int n = nNodes;
    if (order == "vid")
    {
        for (int i = 0; i < n; i++)

            // if i is not a sink
            if (sids.find(i) == sids.end())
                vs.push_back(i);
    }
    else if (order == "desc_deg")
    {
        vs = degOrdDesc(&graph, &sids);
    }
    else if (order == "random")
    {
        vs = randomOrd(nNodes, &sids);
    }
    return vs;
}

GetKHopBenchmark::GetKHopBenchmark(size_t n, string pth, int k, string o, int nE)
{   
    nNodes = n;
    nExpts = nE;
    path = pth;
    K = k;
    order = o;
    nSinks = 0;
    graph = GetKHopBenchmark::readGraph();
    GetKHopBenchmark::calcAllSinkIds();
    vertexOrder = GetKHopBenchmark::calcOrder(order);
}

void GetKHopBenchmark::calcStats()
{
    double sum = accumulate(execTimes.begin(), execTimes.end(), 0.0);
    mean = sum / execTimes.size();

    vector<double> diff(execTimes.size());
    transform(execTimes.begin(), execTimes.end(), diff.begin(),
                bind2nd(minus<double>(), mean));
    double sq_sum = inner_product(diff.begin(), diff.end(), diff.begin(), 0.0);
    stdev = sqrt(sq_sum / execTimes.size());
}
void GetKHopBenchmark::displayStats()
{
    GetKHopBenchmark::calcStats();

    cout << "Ran GetKHopBenchmark " << nExpts << " times, " << "K=" << K << endl;
    cout << "Traversed " << nNodes << " nodes in " << order << " order" << endl;
    cout << "Average time to complete query: " << mean << " ms." << endl; 
    cout << "Std dev. of time to complete query: " << stdev << " ms." << endl; 
}

void GetKHopBenchmark::runExperiment()
{
    execTimes = vector<double>();
    int nIter = nExpts;
    for (int i = 0; i < nIter; i++) 
        execTimes.push_back(runBenchmark());
}

void GetKHopBenchmark::calcAllSinkIds()
{

    for (size_t i = 0; i < nNodes; i++)
    {
        Vertex start = i;

        if (getNeighboursVector(&start, &graph).empty()) {
            nSinks++;
            sids.insert(start);
        }
    }
}

vector<int> GetKHopBenchmark::getAllSinkIds()
{
    vector<int> vs = vector<int>();
    for (auto it = sids.begin(); it != sids.end(); ++it)
    {
        vs.push_back(*it);
    }
    return vs;
}

void GetKHopBenchmark::printAllSinkIds()
{
    vector<int> vs = vector<int>();
    for (auto it = sids.begin(); it != sids.end(); ++it)
    {
        cout << *it << endl;
    }
}


double GetKHopBenchmark::runBenchmark()
{   
    map<int, vector<Vertex>> khopNeighbours; // maps k -> neighbour vertices for k-hop

    // filter zero out-degree nodes 

    // keep a set of all neighbours seen
    // if the size of the set doesn't change after getting the k-neighbours
    // break

    auto t1 = high_resolution_clock::now();
    // iterate through the nodes in the benchmark specified order
    for (auto source : GetKHopBenchmark::vertexOrder)
    {
        Vertex start = source;
        int k = 1;
        khopNeighbours[k] = getNeighboursVector(&start, &graph);
        while (k < K)
        {
            k += 1;
            khopNeighbours[k] = std::vector<Vertex>();
            for (Vertex v : khopNeighbours[k - 1])
            {
                if (getNeighboursVector(&v, &graph).empty())
                    continue;

                for (Vertex u : getNeighboursVector(&v, &graph))
                    khopNeighbours[k].push_back(u);
            }
        }
        khopNeighbours.clear(); // clear vector and continue to next vertex
    }
    auto t2 = high_resolution_clock::now();

    /* Getting number of milliseconds as a double. */
    duration<double, std::milli> ms_double = t2 - t1;

    return ms_double.count() ;
}

void GetKHopBenchmark::printVertexOrder()
{
    cout << "printing vertex order" << endl;
    int i = 0;
    for (auto v : GetKHopBenchmark::vertexOrder)
    {
        cout << "index: " << i << " vertex: " << v << endl;
        i += 1;
    }
}
