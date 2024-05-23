from collections import defaultdict
from zad1 import adj_matrix
import numpy as np

def DFS_visit(v, graph, d, f, t, stack):
    t[0] += 1
    d[v] = t[0]
    for u in graph[v]:
        if d[u] == -1:
            DFS_visit(u, graph, d, f, t, stack)
    t[0] += 1
    f[v] = t[0]
    stack.append(v)

def components_r(nr, v, new_graph, comp):
    comp[v] = nr
    for u in new_graph[v]:
        if comp[u] == -1:
            components_r(nr, u, new_graph, comp)

def kosaraju_algorithm(adj_matrix):
    n = len(adj_matrix)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                graph[i].append(j)

    d = defaultdict(lambda: -1)
    f = defaultdict(int)
    t = [0]
    stack = []

    print(graph)
    for v in range(n):
        if d[v] == -1:
            DFS_visit(v, graph, d, f, t, stack)
    print(stack)
    new_graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if adj_matrix[j][i] == 1:
                new_graph[i].append(j)

    comp = defaultdict(lambda: -1)
    nr = 0
    while stack:
        v = stack.pop()
        if comp[v] == -1:
            nr += 1
            components_r(nr, v, new_graph, comp)

    print(comp.items()[0])
    # strongly_connected_comp=[]
    # current_comp=[]
    # current_comp.append(comp.items()[0][0])
    # prev_val=comp.items()[0][1]

    # for key, val in comp.items()[1:]:
    #     if val==prev_val:
    #         current_comp.append(key)
    #     else:
    #         strongly_connected_comp.append(current_comp)
    #         current_comp=[]

    # return strongly_connected_comp

result = kosaraju_algorithm(adj_matrix)
print(result)

