#include "GetKHopBenchmark.h"
#include <boost/tokenizer.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/dynamic_bitset.hpp>
#include <regex>
#include <memory>
#include <string>
#include <stdexcept>  // For std::unique_ptr
#include <stdarg.h>  // For va_start, etc.
#include "sys/types.h"
#include "sys/sysinfo.h"
#include "stdlib.h"
#include "stdio.h"
#include "string.h"

int parseLine(char* line){
    // This assumes that a digit will be found and the line ends in " Kb".
    int i = strlen(line);
    const char* p = line;
    while (*p <'0' || *p > '9') p++;
    line[i-3] = '\0';
    i = atoi(p);
    return i;
}

int getValue(){ //Note: this value is in KB!
    FILE* file = fopen("/proc/self/status", "r");
    int result = -1;
    char line[128];

    while (fgets(line, 128, file) != NULL){
        if (strncmp(line, "VmSize:", 7) == 0){
            result = parseLine(line);
            break;
        }
    }
    fclose(file);
    return result;
}

// struct sysinfo memInfo;

// sysinfo (&memInfo);
// long long totalVirtualMem = memInfo.totalram;
// //Add other values in next statement to avoid int overflow on right hand side...
// totalVirtualMem += memInfo.totalswap - memInfo.freeswap;
// totalVirtualMem *= memInfo.mem_unit;

using namespace std;
using namespace boost;
using Graph = compressed_sparse_row_graph<>;
using Vertex = Graph::vertex_descriptor;
using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;
typedef boost::graph_traits<Graph>::adjacency_iterator adjacency_it;
typedef boost::graph_traits<Graph>::vertex_iterator vertex_iter;
typedef Graph::vertex_iterator csr_iter;
// get a vertex's neighbours as a vector
vector<Vertex> GetKHopBenchmark::getNeighboursVector(Vertex *vertex, Graph *graph)
{
    vector<Vertex> vec = vector<Vertex>();
    vertex_iter vit, vend;
    adjacency_it neighbour, neighbour_end;
    // for (auto [neighbor, end] = adjacent_vertices(*vertex, *graph); neighbor != end; ++neighbor)
    for (tie(neighbour, neighbour_end) = adjacent_vertices(*vertex, *graph); neighbour != neighbour_end; ++neighbour)
    {
        vec.push_back(*neighbour);        
    }
    return vec;
}

map<int, int> GetKHopBenchmark::readMap()
{
    size_t vertices = nNodes;
    map<int, int> mp;

    string fullPath = GetKHopBenchmark::path;
    char_separator<char> sep("/");
    tokenizer<char_separator<char>> tokens(fullPath, sep);
    string split_arr [4] = {};
    int i = 0;
    std::regex target("(.txt)+");
    std::regex target1("(shuffled_)+");
    std::string replacement="";
    for (const auto& t : tokens) {
        std::string s2 = std::regex_replace(t, target, replacement);
        std::string s3 = std::regex_replace(s2, target1, replacement);
        split_arr[i] = s3;
        i+=1;
    }
    string graph_name = split_arr[3];
    std::ostringstream path_strm;
    path_strm << "./data/maps/" << graph_name << ".txt";

    ifstream ifs(path_strm.str());

    for (string s; getline(ifs, s);)
    {

        string delimiter = " , ";
        string start = s.substr(0, s.find(delimiter));

        s.erase(0, s.find(delimiter) + delimiter.length());

        int from = stoi(start);
        int to = stoi(s);
        mp[from] = to;
    }

    return mp;
}

Graph GetKHopBenchmark::readGraph()
{
    size_t vertices = nNodes;
    vector<pair<Vertex, Vertex>> edges{};

    ifstream ifs(path);

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

GetKHopBenchmark::GetKHopBenchmark(size_t n, string pth, int k, string o, int nE, int ns, int nR)
{   
    srand(time(0));  // Initialize random number generator.
    nNodes = n;
    nExpts = nE;
    path = pth;
    K = k;
    order = o;
    nSinks = 0;
    nIncomps = 0;
    nSeenAll = 0;
    nSamples = ns;
    nReps = nR;
    graph = GetKHopBenchmark::readGraph();
    cout << "read Graph" << endl;
    sortedWts = GetKHopBenchmark::getVectorWeights();
    cumSumWts = GetKHopBenchmark::buildCumSum();
    GetKHopBenchmark::calcAllSinkIds();
    cout << "Calculated sink Ids" << endl;
    vertexOrder = GetKHopBenchmark::calcOrder(order);
    cout << "Calculated Order" << endl;
}

vector<double> GetKHopBenchmark::getExecTimes()
{
    return execTimes;
}

vector<int> GetKHopBenchmark::getVsSeen()
{
    return vsSeen;
}

vector<vector<double>> GetKHopBenchmark::getRepTimes()
{
    return repTimes;
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

void GetKHopBenchmark::runExperiment()
{
    execTimes = vector<double>();
    vsSeen = vector<int>();
    repTimes = vector<vector<double>>();
    int nIter = nExpts;
    for (int i = 0; i < nIter; i++) 
    {   
        // pair<double, int> expRes = runBenchmark(i);
        pair<vector<double>, int> expRes = runBenchmark(i);
        // execTimes.push_back(expRes.first);
        repTimes.push_back(expRes.first);     
        vsSeen.push_back(expRes.second);       
        cout << "Experiment: " << i <<
        // << " took " << execTimes[i] << " ms " << 
        " saw " << vsSeen[i] << 
        " total vertices." << endl;
    }
}

vector<pair<int, int>> GetKHopBenchmark::getVectorWeights()
{
    vector<pair<int, int>> pairs = vector<pair<int, int>> ();

    csr_iter begin, end;
    tie(begin, end) = vertices(graph);

    for (csr_iter it = begin; it != end; ++it) {
        unsigned edges = out_degree(*it, graph);

        pairs.push_back(make_pair(edges, *it));
    }

    sort(pairs.begin(), pairs.end(), greater<pair<int, int>>());

    return pairs;
} 

vector<int> GetKHopBenchmark::buildCumSum()
{   
    assert (sortedWts.size() > 0);
    // make cumulative sum of weights   
    vector<int> cumsum = vector<int>(nNodes);
    cumsum[0] = sortedWts[0].first;
    for (int i = 1; i < nNodes; i++){
        cumsum[i] = cumsum[i-1] + sortedWts[i].first;
    }

    return cumsum;
}

int GetKHopBenchmark::sample()
{
    int totalWt = cumSumWts.back();
    int value = rand() % totalWt;
    int index = lower_bound(cumSumWts.begin(), cumSumWts.end(), value) - cumSumWts.begin();
    assert (index >= 0 && index < cumSumWts.size());
    
    return sortedWts[index].second;
}

void GetKHopBenchmark::write_vector_to_file(const std::vector<int>& myVector, std::string filename)
{   
    string export_path = path;
    std::ofstream ofs(filename, std::ios::out | std::ofstream::binary);
    std::ostream_iterator<char> osi{ ofs };
    const char* beginByte = (char*)&myVector[0];

    const char* endByte = (char*)&myVector.back() + sizeof(int);
    std::copy(beginByte, endByte, osi);
}

std::vector<int> GetKHopBenchmark::read_vector_from_file(std::string filename)
{
    std::vector<char> buffer{};
    std::ifstream ifs(filename, std::ios::in | std::ifstream::binary);
    std::istreambuf_iterator<char> iter(ifs);
    std::istreambuf_iterator<char> end{};
    std::copy(iter, end, std::back_inserter(buffer));
    std::vector<int> newVector(buffer.size() / sizeof(int));
    memcpy(&newVector[0], &buffer[0], buffer.size());
    return newVector;
}

pair<vector<double>, int> GetKHopBenchmark::runBenchmark(int exptNumber)
{   
    vector <Vertex> khopNeighbours[K+1]; // neighbour vertices for kth-hop

    // log execution of query workload
    ofstream out("./log.txt");

    // log growth of neighbour set
    ofstream outCsv("./growth.csv");
    outCsv << "origNode, k, verticesSeen" << endl;

    // iterate through the nodes in the benchmark specified order
    vector<int> ord = vertexOrder;
    vector<int> sampledOrd = vector<int>();

    for (int i = 0; i < nSamples; i++){
        sampledOrd.push_back(sample());
    }
    
    string fullPath = GetKHopBenchmark::path;
    char_separator<char> sep("/");
    tokenizer<char_separator<char>> tokens(fullPath, sep);
    string split_arr [4] = {};
    int i = 0;
    std::regex target("(.txt)+");
    std::regex target1("(shuffled_)+");
    std::string replacement="";
    for (const auto& t : tokens) {
        std::string s2 = std::regex_replace(t, target, replacement);
        std::string s3 = std::regex_replace(s2, target1, replacement);
        cout << s3 << " " << endl;

        split_arr[i] = s3;
        i+=1;
    }
    string graph_name = split_arr[3];
    std::ostringstream path_strm;
    path_strm << "./data/orderings/" << graph_name << "_" << exptNumber;

    // keep a set of all neighbours seen
    // if the size of the set doesn't change after getting the k-neighbours
    // break
    
    if (order == "vid"){
        write_vector_to_file(sampledOrd, path_strm.str());
    }
    if (order == "random") {

        std::vector<int> read_vector = read_vector_from_file(path_strm.str());

        map<int, int> rmp = readMap();
        
        sampledOrd.clear();
        for (auto v : read_vector)
        {
            sampledOrd.push_back(rmp[v]);
        }
        // sampledOrd = read_vector;
    }

    dynamic_bitset<> verticesSeen(nNodes);
    int totalVsSeen = 0;
    // store the runtimes for each repetition
    vector<double> runtimes = vector<double>();

    for (int repNum = 0; repNum < nReps; repNum++)
    {
        cout << "Experiment number: " << exptNumber << ", " <<
        "Rep number: " << repNum << endl;
        
        auto t1 = high_resolution_clock::now();
        for (auto it = sampledOrd.begin(); it != sampledOrd.end(); it++)
        {   
            verticesSeen.reset();
            bool goToNextVertex = false;
            Vertex start = *it;

            int k = 1;
            khopNeighbours[k] = getNeighboursVector(&start, &graph);

            // out << "query workload for vertex: " << start << endl;
            // out << "k = " << k << endl;
            
            for (Vertex u : getNeighboursVector(&start, &graph))
            {   
                // out << k << " hop neighbour: " << u << endl;
                verticesSeen[u] = 1;
                totalVsSeen += 1;            
            }

            // outCsv << start << "," << k << "," << verticesSeen.count()
                    // << "," << endl;
            // int currValue = getValue();
            while (k < K)
            {
                size_t oldSize = verticesSeen.count();
                k += 1;
                // out << "\tk = " << k << endl;

                for (Vertex v : khopNeighbours[k - 1])
                {
                    if (getNeighboursVector(&v, &graph).empty())
                        continue;

                    for (Vertex u : getNeighboursVector(&v, &graph))
                    {   
                        // if we havent seen this vertex yet, add it to kth list of 
                        // neighbours 
                        if (!verticesSeen[u])
                        {
                            // out << "\t" << k << " hop neighbour: " << u << endl;
                            khopNeighbours[k].push_back(u);
                            verticesSeen[u] = 1;
                            totalVsSeen += 1; 
                        }
                    }
                }

                // outCsv << start << "," << k << "," << verticesSeen.count() << "," << endl;
                // break the query if no new neighbours were seen
                if (oldSize == verticesSeen.count()){
                    nIncomps++;
                    if (int(oldSize) == nNodes) nSeenAll++;
                    goToNextVertex = true;
                    break;
                }
            }
            // int afterValue = getValue();

            // clear vector and continue to next vertex
            for (int k = 0; k < K; k++) khopNeighbours[k].clear();
            if (goToNextVertex) {
                // verticesSeen.reset();
                continue;
            }
        }
        auto t2 = high_resolution_clock::now();

        /* Getting number of milliseconds as a double. */
        duration<double, std::milli> ms_double = t2 - t1;
        runtimes.push_back(ms_double.count());
    }
    
    // return make_pair(ms_double.count(), verticesSeen.count());
    return make_pair(runtimes, totalVsSeen);
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


