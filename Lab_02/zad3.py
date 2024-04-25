from zad1 import G, draw
from zad2 import randomize_graph


def bfs(G, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        for neighbor in G[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


def coherent_G_el(G):
    coherent_list_of_all = []
    visited = set()
    for node in G.nodes():
        if node not in visited:
            curr_coherent = bfs(G, node)
            coherent_list_of_all.append(curr_coherent)
            visited.update(curr_coherent)
    return coherent_list_of_all

G=randomize_graph(G)
draw(G)

coherent_list_of_all = coherent_G_el(G)
print(coherent_list_of_all)
