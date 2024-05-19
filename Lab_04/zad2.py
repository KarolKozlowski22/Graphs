import zad1
from collections import defaultdict

t = 0

def DFS(G, v, visited, performed):
    global t
    t = t + 1
    visited[v] = t
    for i in G[v]:
        if visited[i] == -1:
            DFS(G, i, visited, performed)
    t = t + 1
    performed[v] = t

def transform_graph(G):
    G_t = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            G_t[j].append(i)
    return G_t

def components(n, i, G, comp):
    for j in G[i]:
        if comp[j] == -1:
            comp[j] = n
            components(n, j, G, comp)

def kosoraju_algorithm(G):
    visited = [-1] * len(G)
    performed = [-1] * len(G)

    for i in range(len(G)):
        if visited[i] == -1:
            DFS(G, i, visited, performed)

    G_t = transform_graph(G)

    n = 0
    comp = [-1] * len(G)

    performed = [(x, i) for i, x in enumerate(performed)]
    performed.sort(reverse = True, key = lambda x: x[0])

    for val, i in performed:
        if comp[i] == -1:
            n = n + 1
            comp[i] = n
            components(n, i, G_t, comp)

    results = defaultdict(list)
    for i, el in enumerate(comp):
        results[el].append(i)
    
    print(results)

if __name__ == "__main__":
    G = zad1.directed_graph(5, 0.3)
    zad1.draw(G, 5)
    kosoraju_algorithm(G)