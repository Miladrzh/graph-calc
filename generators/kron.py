import random
import string

import snap
import numpy

def generate_graph(node_count, edge_count, abcd=(0.57, 0.19, 0.19, 0.05),
                   save_in_db=True,
                   original_indices=True,
                   shuffled_indices=True,
                   dir='./data/generated-graphs/'):
    Graph = get_rmat_graph_object(node_count, edge_count, abcd)

    from stats.stats import calc
    stats = calc(Graph)

    graph_attr = {'node_count': node_count, 'edge_count': edge_count, 'generate_method': 'SNAP_RMAT', **stats}

    file_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
    print(file_hash)

    if original_indices:
        with open(dir + file_hash + '.txt', "w+") as file:
            for EI in Graph.Edges():
                file.write("%d , %d\n" % (EI.GetSrcNId(), EI.GetDstNId()))
            file.close()
        if save_in_db:
            from storage.models import GeneratedGraph
            graph_attr = {**graph_attr, 'file_hash': file_hash, 'ordering': 'default'}
            GeneratedGraph.objects.create(**graph_attr)

    if shuffled_indices:
        indices_map = numpy.random.permutation(node_count)

        ts = [(indices_map[EI.GetSrcNId()], indices_map[EI.GetDstNId()]) for EI in Graph.Edges()]

        ts = sorted(ts)

        with open(dir + 'shuffled_' + file_hash + '.txt', "w+") as file:
            for EI in ts:
                file.write("%d , %d\n" % (EI[0], EI[1]))
            file.close()
        if save_in_db:
            from storage.models import GeneratedGraph
            graph_attr = {**graph_attr, 'file_hash': 'shuffled_' + file_hash, 'ordering': 'shuffle_random'}
            GeneratedGraph.objects.create(**graph_attr)

    del Graph

def get_rmat_graph_object(node_count, edge_count, abcd):
    Rnd = snap.TRnd(random.randint(1, 1000000))
    Graph = snap.GenRMat(
        node_count, edge_count, float(abcd[0]), float(abcd[1]), float(abcd[2]), Rnd)
    return Graph