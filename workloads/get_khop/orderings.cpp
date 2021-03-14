#include "orderings.h"

// thanks to https://stackoverflow.com/a/5056797
template <typename A, typename B>
std::pair<B, A> flip_pair(const std::pair<A, B> &p)
{
    return std::pair<B, A>(p.second, p.first);
}

template <typename A, typename B>
std::multimap<B, A> flip_map(const std::map<A, B> &src)
{
    std::multimap<B, A> dst;
    std::transform(src.begin(), src.end(), std::inserter(dst, dst.begin()),
                   flip_pair<A, B>);
    return dst;
}

// map all vertices to their degrees
std::map<int, int> getDegrees(Graph *graph)
{
    Graph::vertex_iterator v, vend;
    std::map<int, int> degs;
    for (boost::tie(v, vend) = boost::vertices(*graph); v != vend; ++v)
        degs[*v] = boost::out_degree(*v, *graph);
    return degs;
}

std::map<int, int> degreeDistribution(Graph *graph)
{
    Graph::vertex_iterator v, vend;
    std::map<int, int> dist;
    for (boost::tie(v, vend) = boost::vertices(*graph); v != vend; ++v)
    {
        int deg = boost::out_degree(*v, *graph);
        if (dist.find(deg) == dist.end())
            dist[deg] =1;
        else 
            dist[deg] += 1;
    }
    return dist;
    
}

// order vertices by degree (descending)
std::vector<int> degOrdDesc(Graph *graph)
{
    std::vector<int> values;
    std::map<int, int> outDeg = getDegrees(graph);
    std::multimap<int, int> revOutDeg = flip_map(outDeg);

    for (std::map<int, int>::iterator it = revOutDeg.begin(); it != revOutDeg.end(); ++it)
    {
        values.push_back(it->second);
    }
    std::reverse(values.begin(), values.end());
    return values;
}

// order vertices randomly
// generate a random permutation of 0 to nVertices
std::vector<int> randomOrd(int nVertices)
{
    std::srand(unsigned(std::time(0)));
    std::vector<int> perm;

    // set some values:
    for (int i = 1; i < nVertices; ++i)
        perm.push_back(i); 

    // using built-in random generator:
    std::random_shuffle(perm.begin(), perm.end());

    return perm;
}
