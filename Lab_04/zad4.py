"""
Zaimplementować algorytm Johnsona do szukania odległości pomiędzy
 wszystkimi parami wierzchołków na ważonym grafie skierowanym.
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd


def generate_digraph(n, p):
    G = nx.DiGraph()
    G.add_nodes_from(range(n))

    for i in range(n):
        for j in range(n):
            if i != j:
                if random.random() < p:
                    G.add_edge(i, j, weight=random.randint(-2, 10))
    return G


def draw_graph_with_weights(G, filename):
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    # Draw edges with different styles and labels for each direction
    # edge_labels = nx.get_edge_attributes(G, 'weight')
    for (u, v, d) in G.edges(data=True):
        if 'weight' in d:
            if G.has_edge(v, u):
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], arrowstyle='->',
                                       arrowsize=20, edge_color='black')
                nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight']}, label_pos=0.2,
                                             font_color='blue')
            else:
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], arrowstyle='->',
                                       arrowsize=20, edge_color='black')
                nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight']}, label_pos=0.2,
                                             font_color='blue')

    plt.savefig(filename)
    plt.close()


def add_s(G):
    G_prim = G.copy()
    G.add_node('s')
    for node in G.nodes():
        if node != 's':
            G_prim.add_edge('s', node, weight=0)
    return G_prim


def johnson(G):
    G_prim = add_s(G)

    # slownik : odleglosci od node 's' do reszty h[1] = 0 - odleglosc z 's' do 1 to 0
    try:
        h = nx.single_source_bellman_ford_path_length(G_prim, 's')
    except nx.NetworkXUnbounded:
        raise ValueError("Graph contains a negative weight cycle")

    draw_graph_with_weights(G_prim, "original.png")
    print(h)

    # reweight edges
    for u, v, data in G_prim.edges(data=True):
        data['weight'] += h[u] - h[v]
    draw_graph_with_weights(G_prim, "reweighted.png")
    G_prim.remove_node('s')
    draw_graph_with_weights(G_prim, "withouts.png")
    print("Is strongly connected g prim: ", nx.is_strongly_connected(G_prim))

    distances = {}
    for node in G_prim.nodes():
        dist = nx.single_source_dijkstra_path_length(G_prim, node)
        distances[node] = {v: dist[v] - h[node] + h[v] for v in dist}

    return distances


if __name__ == "__main__":
    graph = generate_digraph(5, 0.7)
    draw_graph_with_weights(graph, "before.png")
    print("Is strongly connected: ", nx.is_strongly_connected(graph))

    D = johnson(graph)
    print("\nDistances:")
    df = pd.DataFrame(D).T
    print(df)

