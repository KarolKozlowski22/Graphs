import networkx as nx
from Lab_02.zad1 import draw
from collections import defaultdict
import numpy as np


def random_regular_graph(d, n, seed=None):
    if (n * d) % 2 != 0:
        raise nx.NetworkXError("n * d must be even")

    if not 0 <= d < n:
        raise nx.NetworkXError("the 0 <= d < n inequality must be satisfied")

    if d == 0:
        return nx.empty_graph(n)

    def _suitable(edges, potential_edges):
        if not potential_edges:
            return True
        for s1 in potential_edges:
            for s2 in potential_edges:

                if s1 == s2:
                    break
                if s1 > s2:
                    s1, s2 = s2, s1
                if (s1, s2) not in edges:
                    return True
        return False

    def _try_creation():

        edges = set()
        stubs = list(range(n)) * d

        while stubs:
            potential_edges = defaultdict(lambda: 0)
            seed.shuffle(stubs)
            stubiter = iter(stubs)
            for s1, s2 in zip(stubiter, stubiter):
                if s1 > s2:
                    s1, s2 = s2, s1
                if s1 != s2 and ((s1, s2) not in edges):
                    edges.add((s1, s2))
                else:
                    potential_edges[s1] += 1
                    potential_edges[s2] += 1

            if not _suitable(edges, potential_edges):
                return None

            stubs = [
                node
                for node, potential in potential_edges.items()
                for _ in range(potential)
            ]
        return edges

    edges = _try_creation()
    while edges is None:
        edges = _try_creation()

    G = nx.Graph()
    G.add_edges_from(edges)

    return G


n = 10
k = 3

G = random_regular_graph(k, n, seed=np.random.default_rng())
draw(G)
