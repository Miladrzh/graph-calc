from generators.kron import generate_graph

node_count_list = [2 ** i for i in range(18, 19)]
edge_factor_list = [i for i in range(5, 6)]

for node_count in node_count_list:
    for edge_factor in edge_factor_list:
        for i in range(1, 20):
            generate_graph(node_count, edge_factor * node_count, original_indices=False)
            generate_graph(node_count, edge_factor * node_count, original_indices=False)
            generate_graph(node_count, edge_factor * node_count, original_indices=False)
