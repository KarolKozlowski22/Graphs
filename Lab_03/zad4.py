import numpy as np
from zad3 import gen_distance_matrix

"""
Wyznaczyć centrum grafu, to znaczy wierzchołek, którego suma odległości do pozostałych wierzchołków jest
minimalna. Wyznaczyć centrum minimax, to znaczy wierzchołek, którego odległość do najdalszego wierzchołka jest
minimalna.

"""


def get_centrum(graph, w):
    sums = []
    distance_matrix = gen_distance_matrix(graph, w)
    for row in distance_matrix:
        sums.append(sum(row))

    min_sum = np.inf
    min_index = None
    for i in range(len(sums)):
        if sums[i] < min_sum:
            min_sum = sums[i]
            min_index = i

    return min_index


def get_centrum_minimax(graph, w):
    distance_matrix = gen_distance_matrix(graph, w)
    dists = [max(row) for row in distance_matrix]
    min_dist = np.inf
    min_index = None
    for i in range(len(dists)):
        if dists[i] < min_dist:
            min_dist = dists[i]
            min_index = i

    return min_index

