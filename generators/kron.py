import random
import string

import snap
import numpy


def generate_and_save_graph(node_count=None, edge_count=None):
    from storage.models import GeneratedGraph
    file_hash, node_count, edge_count = generate_graph(node_count, edge_count)
    GeneratedGraph.objects.create(file_hash=file_hash, generate_method='SNAP_RMAT', node_count=node_count,
                                  edge_count=edge_count)


def generate_graph(node_count=None, edge_count=None, dir='./data/generated-graphs/'):
    if node_count is None:
        node_count = random.randint(300, 10000)  # TODO assumption
    if edge_count is None:
        edge_count = random.randint(node_count, 1000000)  # TODO assumption

    abcd = numpy.random.random(4)
    abcd /= abcd.sum()
    Rnd = snap.TRnd(random.randint(1, 1000000))

    file_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
    print(file_hash)
    with open(dir + file_hash + '.txt', "w+") as file:
        Graph = snap.GenRMat(node_count, edge_count, float(abcd[0]), float(abcd[1]), float(abcd[2]), Rnd)
        for EI in Graph.Edges():
            file.write("%d , %d\n" % (EI.GetSrcNId(), EI.GetDstNId()))
        file.close()
    return file_hash, node_count, edge_count
