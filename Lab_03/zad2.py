import numpy as np
import networkx as nx

"""
Zaimplementować algorytm Dijkstry do znajdowania najkrótszych ścieżek od
zadanego wierzchołka do pozostałych wierzchołków i zastosować go do grafu
z zadania pierwszego, w którym wagi krawędzi interpretowane są jako odległości
wierzchołków. Wypisać wszystkie najkrótsze ścieżki od danego wierzchołka i ich
długości.
"""


def init(G: nx.graph, s):
    d = []
    p = []
    for v in G.nodes():
        d.append(np.inf)  # nodes start from 0, not 1
        p.append(None)
    d[s] = 0
    return d, p


# u, v - nodes with the edge to relax
# w - weight matrix
# d & p - lists from above
def relax(u, v, w, d, p):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        p[v] = u


def dijkstra(G: nx.Graph, w, s):
    d, p = init(G, s)
    S = []
    u = None
    while len(S) != len(G.nodes):
        min_d = np.inf
        for v in G.nodes:
            if v not in S and d[v] < min_d:
                u = v
                min_d = d[v]
        S.append(u)
        for v in G.neighbors(u):
            if v not in S:
                relax(u, v, w, d, p)
    return d, s


# d[u] - długość najkrótszej ścieżki z wierzchołka startowego s do wierzchołka u
# p[u] - poprzednik wierzchołka u na najkrótszej ścieżce z s do u

"""
d:  [0, 9, 1, 2, 4, 1, 3]
taki wynik dla wierzcholka 0 oznacza ze:
najkrotsza sciezka z 0 do 0 to 0
najkrotsza sciezka z 0 do 1 to 9
najkrotsza sciezka z 0 do 2 to 1
...
"""
