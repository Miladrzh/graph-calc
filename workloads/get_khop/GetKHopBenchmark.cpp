#include "GetKHopBenchmark.h"

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
    // skip the first four commented lines
    string dummyLine;
    for (int i = 0; i < 4; i++)
        getline(ifs, dummyLine);
    // read graph
    for (string s; getline(ifs, s);)
    {
        int from, to;
        if (istringstream(s) >> from >> to)
            edges.emplace_back(from, to);
        else
            break;
    }

    Graph graph{edges_are_sorted, edges.begin(), edges.end(), vertices};
    return graph;
}

vector<int> GetKHopBenchmark::calcOrder(string order)
{
    vector<int> v = vector<int>{};
    int n = nNodes;
    if (order == "vid")
    {
        for (int i = 0; i < n; i++)
            v.push_back(i);
    }
    else if (order == "desc_deg")
    {
        v = degOrdDesc(&graph);
    }
    else if (order == "random")
    {
        v = randomOrd(nNodes);
    }
    return v;
}

GetKHopBenchmark::GetKHopBenchmark(int n, string pth, int k, string o, int nE)
{
    nNodes = n;
    nExpts = nE;
    path = pth;
    K = k;
    order = o;
    vertexOrder = GetKHopBenchmark::calcOrder(order);
    graph = GetKHopBenchmark::readGraph();
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

double GetKHopBenchmark::runBenchmark()
{   
    map<int, vector<Vertex>> khopNeighbours; // maps k -> neighbour vertices for k-hop

    auto t1 = high_resolution_clock::now();
    // iterate through the nodes in the benchmark specified order
    for (auto source : GetKHopBenchmark::vertexOrder)
    {
        // cout << "source: " <<  source << endl;
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
            // cout << "\t" << k << endl;
            // for (auto n: khopNeighbours[k]) 
            //     cout  << "\t\t" << n << endl;
        }
        khopNeighbours.clear(); // clear map and continue to next vertex
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
