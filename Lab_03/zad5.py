import networkx as nx
import numpy as np

"""
Wyznaczyć minimalne drzewo rozpinające (algorytm Prima lub Kruskala).
"""


def prim(graph: nx.graph, start_node):
    T = [start_node]  # tu bedzie drzewo najmniejsze sie rozpinac
    W = list(graph.nodes)  # a z tego bedziemy usuwac jak juz pojdzie do drzewa
    W.remove(start_node)

    while len(T) != len(graph.nodes):
        min_weight = np.inf
        next_node = None
        for neighbor in graph.neighbors(start_node):
            if neighbor in W:
                edge_weight = graph.get_edge_data(start_node, neighbor)['weight']
                if edge_weight < min_weight:
                    min_weight = edge_weight
                    next_node = neighbor

        T.append(next_node)
        W.remove(next_node)
        start_node = next_node

    return T


# sortowanie krawedzi po wagach i branie takich zeby nie powstaly cykle
def kruskal(graph):
    edges = [(graph.edges[u, v]['weight'], u, v) for u, v in graph.edges()]
    edges.sort()
    mst = []
    parent = {node: node for node in graph.nodes()}

    # sprawdza czy sie nie stworzy cykl
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for weight, u, v in edges:
        if find(u) != find(v):
            mst.append((u, v))
            union(u, v)

    return mst


