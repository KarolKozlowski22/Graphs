import random

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from networkx import draw_circular

from Lab_02.zad5 import random_regular_graph

"""
Korzystając z programów z poprzednich zestawów wygenerować spójny
graf losowy. Przypisać każdej krawędzi tego grafu losową wagę będącą
liczbą naturalną z zakresu 1 do 10.
"""


def gen_connected_graph_with_wages(n, k):
    graph = random_regular_graph(k, n, seed=np.random.default_rng())
    edge_weights = {}
    weight_matrix = np.full((n, n), 0)
    for u, v in graph.edges():
        weight = random.randint(1, 10)
        graph.edges[u, v]['weight'] = weight
        edge_weights[(u, v)] = weight
        weight_matrix[u][v] = weight
        weight_matrix[v][u] = weight  # Jeśli graf jest nieskierowany, wagi są symetryczne

    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weights)
    plt.show()
    return graph, weight_matrix


