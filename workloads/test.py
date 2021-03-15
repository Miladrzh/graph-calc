import workloads.get_khop.GetKHopBenchmark as B
import numpy as np
from generators import kron
import os
import pandas as pd

path = '../data/generated-graphs/2tb5pijfnyg3vpkk.txt'

def run_test():
    ns = [2**i for i in np.linspace(10, 20, 11)]
    ns = [i*1000 for i in range(1,10)]
    ns = [1000, 5000, 10000, 50000, 100000]
    ns = [50000, 100000]

    params = {}
    for n in ns:
        params[n] = []
        for factor in [2, 5, 15, 25, 50]:
            params[n].append(n*factor)
    print(params)

    # generate a set of increasingly bigger graphs

    # for n_nodes, n_edges_list in params.items():
    #     for n_edges in n_edges_list:
    #         print(n_nodes, n_edges)
    #         kron.generate_and_save_graph(n_nodes, n_edges)
    # return
    # get all the graph currently in db
    from storage.models import GeneratedGraph
    all_entries = GeneratedGraph.objects \
        .filter(edge_count__exact=1000) 
        # .filter(node_count__gte=500000) \
    # all_entries = GeneratedGraph.objects.filter(node_count__lt=500000)
    props = [(e.file_hash, e.node_count, e.edge_count) for e in all_entries]
    print(props)
    
    prop = props[0]
    path = os.path.join('./data', 'generated-graphs',
            prop[0] + '.txt')
    print(f"running benchmark on {path}")
    node_count = prop[1]
    edge_count = prop[2]
    bmark = B.GetKHopBenchmark(node_count, path, 3, "desc_deg", 100)

    bmark.printAllSinkIds()
    print(bmark.nSinks)
    bmark.printVertexOrder()
    # bmark.runExperiment()
    # bmark.calcStats()

    return

    orders = ['vid', 'random',]
    i = 0
    ks = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ks = [3, 4, 5, 6, 7, 8, 9, 10]
    columns = ['node_count', 'edge_count', 'order', 'k', 'mean', 'stdev']

    df = pd.DataFrame(columns=columns)
    
    # take the first 10 hashes and run varied benchmarks on them 
    for prop in props[:]:
        d = {}
        path = os.path.join('../', 'data', 'generated-graphs',
                prop[0] + '.txt')
        print(f"running benchmark on {path}")
        node_count = prop[1]
        edge_count = prop[2]
        
        for order in orders:
            for k in ks:
                # create the benchmark
                bmark = B.GetKHopBenchmark(node_count, path, k, order, 100)
                bmark.runExperiment()
                bmark.calcStats()

                print(bmark.order)
                print(bmark.mean)
                d['node_count'] = node_count
                d['edge_count'] = edge_count
                d['order'] = order
                d['k'] = k
                d['mean'] = bmark.mean
                d['stdev'] = bmark.stdev
                # get the benchmark stats
                df = df.append(d, ignore_index=True)
                del bmark
        # i+=1
        # if i>1:
            # break

    df.to_csv('tmp3.csv')