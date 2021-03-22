import workloads.get_khop.GetKHopBenchmark as B

from storage.models import WorkloadResult

import numpy as np
from generators import kron
import os
import pandas as pd


def run_test():
    ns = [2**i for i in np.linspace(10, 20, 11)]
    ns = [i*1000 for i in range(1,10)]
    ns = [1000, 5000, 10000, 50000, 100000]
    ns = [50000, 100000]
    params = {}
    for n in ns:
        params[n] = []
        for factor in [2, 5, 15,]:
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

    all_entries = GeneratedGraph.objects.filter(edge_count__lte=1500000)
    props = [(e.file_hash, e.node_count, e.edge_count, e.OutDegCnt_std, e.clust_coef) for e in all_entries]
    orders = ['vid', 'random', 'desc_deg']
    order = 'vid'
    i = 0
    ks = [2,3,]
    ks = [2,]
    columns = ['node_count', 'edge_count', 'order', 'k', 'mean', 'stdev', 'n_incompletes', 'n_seen_all', 'n_sinks', 'out_deg_std', 'clust_coef']
    order = 'vid'
    df = pd.DataFrame(columns=columns)
    
    print(props)
    nSamples = 100
    print(props)
    for prop, obj in zip(props[:1], all_entries[:]):
        d = {}
        file_hash = prop[0] 
        path = os.path.join('./', 'data', 'generated-graphs',
                file_hash + '.txt')
        print(f"running benchmark on {path}")
        node_count = prop[1]
        edge_count = prop[2]
        out_deg_std = prop[3]
        clust_coef = prop[4]
    
        for k in ks:
            print("node_count: " + str(node_count))
            print("edge_count: " + str(edge_count))
            print("k: " + str(k))
            # create the benchmark
            bmark = B.GetKHopBenchmark(node_count, path, k, order, 10, nSamples)
            bmark.runExperiment()
            bmark.calcStats()

            exec_times = np.array(bmark.getExecTimes())
            # d['node_count'] = node_count
            # d['edge_count'] = edge_count
            # d['order'] = order
            # d['k'] = k
            # d['mean'] = bmark.mean
            # d['stdev'] = bmark.stdev
            # d['n_incompletes'] = bmark.nIncomps / bmark.nExpts
            # d['n_seen_all'] = bmark.nSeenAll / bmark.nExpts
            # d['n_sinks'] = bmark.nSinks
            # d['out_deg_std'] = out_deg_std
            # d['clust_coef'] = clust_coef
            # # get the benchmark stats
            # df = df.append(d, ignore_index=True)
            exp_num = 1
            for etime in exec_times:
                print(etime)
                print(exp_num)
                # write to workload result model
                WorkloadResult.objects.create(
                    file_hash=obj, 
                    experiment='2HOP',
                    exp_num=exp_num,
                    duration=etime
                )
                exp_num+=1
            del bmark

        # i+=1
        # if i>1:
            # break

    # df.to_csv('./tmp.csv')
