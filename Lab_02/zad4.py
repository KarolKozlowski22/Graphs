import networkx as nx
from matplotlib import pyplot as plt
from networkx import draw_circular, is_eulerian

from zad1 import create_graph, draw
import random

"""
Używając powyższych programów napisać program do tworzenia losowego grafu eulerowskiego i znajdowania na nim
cyklu Eulera
"""


# Nie dziala poprawnie dla wylosowanego grafu
def create_euler_graph():
    num_nodes = random.randint(6, 10)
    A = []
    for i in range(num_nodes):
        A.append(random.choice([2, 4, 6]))
    print(A)
    G = create_graph(A)
    draw_circular(G, with_labels=True)


def fleurys_algorithm(graph):
    if not is_eulerian(graph):
        return "Graf nie jest eulerowski"

    current_node = 0
    neighbors = list(graph.neighbors(current_node))
    next_node = neighbors.pop()
    euler_cycle = [current_node]

    while graph.has_edge(current_node, next_node):
        euler_cycle.append(next_node)
        graph.remove_edge(current_node, next_node)

        if graph.number_of_edges() == 0:
            break

        current_node = next_node
        neighbors = list(graph.neighbors(current_node))
        next_node = neighbors.pop()

    return euler_cycle

# Dla tego grafu dziala dobrze
graph = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [1, 2],
    4: [2]
}

G = nx.Graph(graph)
draw_circular(G, with_labels=True)
plt.show()
euler_cycle = fleurys_algorithm(G)
print("Cykl Eulera:", euler_cycle)
