import random
import string

import snap
import numpy

def generate_and_save_graph(node_count=None, edge_count=None):
    from storage.models import GeneratedGraph
    graph_attr = generate_graph(node_count, edge_count)

    GeneratedGraph.objects.create(
        file_hash=graph_attr['file_hash'], 
        generate_method='SNAP_RMAT', 
        node_count=graph_attr['node_count'],
        edge_count=graph_attr['edge_count']
    )

# def calc_stats()

def generate_graph(node_count=None, edge_count=None, dir='./data/generated-graphs/'):
    from stats.stats import calc
    if node_count is None:
        node_count = random.randint(300, 10000)  # TODO assumption
    if edge_count is None:
        edge_count = random.randint(node_count, 1000000)  # TODO assumption

    abcd = numpy.random.random(4)
    abcd /= abcd.sum()
    Rnd = snap.TRnd(random.randint(1, 1000000))

    file_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))

    # store graph attributes in a dict
    graph_attr = {
        'file_hash': file_hash,
        'node_count': node_count,
        'edge_count': edge_count,
    }

    Graph = snap.GenRMat(
        node_count, edge_count, float(abcd[0]), float(abcd[1]), float(abcd[2]), Rnd)

    stats = calc(Graph);
    graph_attr = {**graph_attr, **stats} # merge stats into graph attributes

    print(file_hash)
    print(graph_attr)
    with open(dir + file_hash + '.txt', "w+") as file:
        for EI in Graph.Edges():
            file.write("%d , %d\n" % (EI.GetSrcNId(), EI.GetDstNId()))
        file.close()
    return graph_attr
