"""
Napisać program do generowania losowych grafów k-regularnych.
Graf k-regularny – graf, którego każdy wierzchołek ma stopień równy k.

"""
import math

from networkx import Graph, draw_circular, empty_graph
import matplotlib.pyplot as plt


# n - number of nodes
# k - degree
def generate_k_degree_regular_graph(n, k):
    if n <= k:
        return
    if (n * k) % 2 != 0:
        return
    if k == 0:
        return empty_graph(n)

    graph = Graph()
    graph.add_nodes_from(range(n))

    for i in range(int(n)):
        for j in range(math.ceil(k/2)):
            l = (i + 1 + j) % n
            if graph.degree(i) < k and graph.degree(l) < k:
                graph.add_edge(i, l)
    return graph


# dla (7,3) calkiem sie wywala, dla (6,3) zle generuje, nie wiem jak ten algorytm ma wygladac tak szczerze
graph = generate_k_degree_regular_graph(8, 3)
draw_circular(graph, with_labels=True)
plt.show()
