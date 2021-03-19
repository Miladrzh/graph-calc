import workloads.get_khop.GetKHopBenchmark as B
import numpy as np
from generators import kron
import os
import pandas as pd


def run_test():
    ns = [2**i for i in np.linspace(10, 20, 11)]
    ns = [i*1000 for i in range(1,10)]
    ns = [1000, 5000, 10000, 50000, 100000]

    params = {}
    for n in ns:
        params[n] = []
        for factor in [2, 5, 15, 25,]:
            params[n].append(n*factor)
    print(params)
    # generate a set of increasingly bigger graphs

    # for n_nodes, n_edges_list in params.items():
    #     for n_edges in n_edges_list:
    #         print(n_nodes, n_edges)
    #         kron.generate_graph(n_nodes, n_edges, 
    #         abcd=[.57, .19, .19])
    # return

    # get all the graph currently in db
    from storage.models import GeneratedGraph
    all_entries = GeneratedGraph.objects.filter(node_count__lt=2500000)
    props = [(e.file_hash, e.node_count, e.edge_count) for e in all_entries]

    orders = ['vid', 'random', 'desc_deg']
    order = 'vid'
    i = 0
    ks = [2,3,]
    columns = ['node_count', 'edge_count', 'order', 'k', 'mean', 'stdev', 
                'n_incompletes', 'n_seen_all', 'n_sinks']

    df = pd.DataFrame(columns=columns)
    
    # filter all shuffled versions for now
    props = [p for p in props if 'shuffled' not in p[0]]
    print(props)
    # take the first 10 hashes and run varied benchmarks on them 
    for prop in props[:]:
        d = {}
        path = os.path.join('./', 'data', 'generated-graphs',
                prop[0] + '.txt')
        print(f"running benchmark on {path}")
        node_count = prop[1]
        edge_count = prop[2]
        
        for k in ks:
            # create the benchmark
            print(node_count, path, k, "vid", 25)
            bmark = B.GetKHopBenchmark(node_count, path, k, "vid", 25)
            print(bmark)
            bmark.runExperiment()
            bmark.calcStats()

            print(bmark.order)
            print(k)
            print(bmark.mean)
            print(bmark.nSinks)
            print(bmark.nIncomps / bmark.nExpts)
            print(bmark.nSeenAll / bmark.nExpts)
            d['node_count'] = node_count
            d['edge_count'] = edge_count
            d['order'] = order
            d['k'] = k
            d['mean'] = bmark.mean
            d['stdev'] = bmark.stdev
            d['n_incompletes'] = bmark.nIncomps / bmark.nExpts
            d['n_seen_all'] = bmark.nSeenAll / bmark.nExpts
            d['n_sinks'] = bmark.nSinks
            # get the benchmark stats
            df = df.append(d, ignore_index=True)
            del bmark
        # i+=1
        # if i>1:
            # break

    df.to_csv('./tmp.csv')