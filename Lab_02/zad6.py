import networkx as nx
from matplotlib import pyplot as plt
from networkx import draw_circular

def dfs(graph, current, visited):
    if len(visited) == len(graph.nodes):
        if graph.has_edge(current, visited[0]):
            return True
        else:
            return False

    for neighbor in graph.neighbors(current):
        if neighbor not in visited:
            visited.append(neighbor)
            if dfs(graph, neighbor, visited):
                return True
            visited.pop()

    return False


def hamiltonian_cycle(graph: nx.Graph):
    # twierdzenie Diraca
    if graph.number_of_nodes() > 2 and all(graph.degree(n) >= n / 2 for n in graph.nodes()):
        print("Twierdzenie Diraca spelnione")

    for node in graph.nodes():
        visited = [node]
        if dfs(graph, node, visited):
            return visited

    print("brak cyklu Hamiltona")
    return False


G2 = nx.Graph()
G2.add_edges_from([(1, 3), (1, 5), (1, 6), (2, 6), (2, 4), (2, 5), (3, 5), (4, 5)])
draw_circular(G2, with_labels=True)
plt.show()
cycle = hamiltonian_cycle(G2)
if cycle:
    print("Cykl Hamiltona: ", cycle)
