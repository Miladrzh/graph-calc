# this script is used for generating graph at the first phase
# Rmat matrix would be [0.57, 0.19, 0.19, 0.05]
# graph has node_count in {1000, 1100, ... , 10000}
# graph has edge_count {node_count, 2*node_count, 3*node_count, ... 50*node_count}
# generating 3 graphs per each combination of (node_count, edge_count)
# Total number of
from generators.kron import generate_and_save_graph

abcd = [0.57, 0.19, 0.19, 0.05]
for node_count in range(10 ** 3, 10 ** 5 + 1, 10 ** 2):
    for edge_count in range(node_count, 50 * node_count, node_count):
        generate_and_save_graph(node_count, edge_count, abcd)
        generate_and_save_graph(node_count, edge_count, abcd)
        generate_and_save_graph(node_count, edge_count, abcd)
        print(node_count, edge_count)
