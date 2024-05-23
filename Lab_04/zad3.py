# Wykorzystując algorytmy z powyższych punktów wygenerować losowy
# silnie spójny digraf. Łukom tego digrafu przypisać losowe wagi będące
# liczbami całkowitymi z zakresu [−5, 10]. Zaimplementować algorytm
# Bellmana-Forda do znajdowania najkrótszych ścieżek od danego wierzchołka.

from zad1 import directed_graph, print_graph, draw
from zad2 import DFS, kosoraju_algorithm
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


def draw_with_wages(G, log=True):
    n = len(G)
    graph = nx.DiGraph()
    for i in range(n):
        for j, wage in G[i]:
            graph.add_edge(i, j, weight=wage)

    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    filename = "graph_with_wages.png"
    plt.savefig(filename)
    plt.close()

    if log:
        print_graph(graph_with_wages)


def add_wages(graph, rand_start = -2, rand_end = 10):
    new_graph = [[] for _ in range(len(graph))]  
    for i, row in enumerate(graph):  
        for j, e in enumerate(row):
            random_value = randint(rand_start, rand_end)  
            new_graph[i].append((e, random_value))
    return new_graph


def Bellman_Ford(G, s):
    n = len(G)
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
    return d


if __name__ == "__main__":
    n = 5
    p = 0.2
    s = 4

    graph = directed_graph(n, p)
    while(kosoraju_algorithm(graph) != 1):
        graph = directed_graph(n, p)           #generowanie silnie spojnego

    graph_with_wages = add_wages(graph)
    print(f"\nStart vertex: [(end vertex, distance)] ")
    draw_with_wages(graph_with_wages)

    distances_for_s = Bellman_Ford(graph_with_wages, s)
    print(f"\nDistances from vertex {s} to: ")
    res_tab = {i: dist for i, dist in enumerate(distances_for_s)}
    print(res_tab, sep=", ")
