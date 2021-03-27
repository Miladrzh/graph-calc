import numpy as np
from scipy.special import comb
from generators import kron
from stats.stats import get_hist_array
import json

def expected_n_vs_w_degree(k, n_edges, n, p=0.76):
    """calculate the expected number of nodes with in/out degree k
    
    from R-MAT: A Recursive Model for Graph Mining
    https://www.cs.cmu.edu/~christos/PUBLICATIONS/siam04.pdf

    Args:
        k (int): in/out-degree
        n_edges (int): number of edges in graph
        n (int): 2^{n} is the number of nodes in the RMAT graph
        p (double): given the probabilities of an edge falling into partitions
            in the R-MAT model abcd=0.57, 0.19, 0.19, 0.05, and a+b+c+d = 1
            use p = a+b for expected number of nodes with outdegree k
            use p = a+c for expected number of nodes with indegree k
            default = 0.57+0.19 = 0.76
    """
    def prob(n, i, p, k, n_edges):
        return comb(n, i) * \
            np.power(np.power(p, n-i) * np.power(1-p, i), k) * \
            np.power(1 - np.power(p, n-i) * np.power(1-p, i), n_edges-k)
    
    exp_n = \
        comb(n_edges, k) * \
        np.sum([prob(n, i, p, k, n_edges) for i in range(0, n+1)])
    return exp_n

def run_test():
    # generate a set of graphs
    ns = [2**i for i in range(10,14)]
    es = [2**i for i in range(11,15)]
    max_k = 20

    for n_nodes, n_edges in zip(ns, es):
        n = int(np.log2(n_nodes))
        abcd=(0.57, 0.19, 0.19, 0.05)
        Graph = kron.get_rmat_graph_object(n_nodes, n_edges, abcd=abcd)
        OutDegCnt = get_hist_array(Graph.GetOutDegCnt())
        a = abcd[0]
        b = abcd[1]
        c = abcd[2]
        res = {}

        for i in range(OutDegCnt.shape[0]):
            k = OutDegCnt[i][0]
            if k > max_k:
                break
            else:
                actual_n = OutDegCnt[i][1]
                exp_n = expected_n_vs_w_degree(k, n_edges, n, p=a+b)
                res[str(k)] = {
                    'actual': int(actual_n),
                    'expected': float(exp_n)
                }

        
        print(json.dumps(res, sort_keys=True, indent=4))