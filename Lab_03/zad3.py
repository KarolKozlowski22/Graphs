import numpy as np
from zad2 import dijkstra
from zad1 import gen_connected_graph_with_wages

"""
 Wyznaczyć macierz odległości miedzy wszystkimi parami wierzchołków
na tym grafie.
"""


def gen_distance_matrix(graph, w):
    nodes_num = len(graph.nodes)
    distance_matrix = np.full((nodes_num, nodes_num), 0)

    for i in range(nodes_num):
        d, p = dijkstra(graph, w, i)
        distance_matrix[i] = d

    return distance_matrix


