import networkx as nx
import matplotlib.pyplot as plt
import random
from zad1 import graph_visualization

def ford_fulkerson_mine(G, s, t):
    f = {(u, v): 0 for u, v in G.edges()}
    
    def cf(u, v):
        return G[u][v]['capacity'] - f[(u, v)]
    
    def bfs(Gf, s, t):
        queue = [s]
        visited = {s}
        parent = {}
        while queue:
            u = queue.pop(0)
            for v in Gf[u]:
                if v not in visited and cf(u, v) > 0:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == t:
                        return True, parent
        return False, parent
    
    while True:
        found_path, parent = bfs(G, s, t)
        if not found_path:
            break
        min_flow = min(cf(u, v) for u, v in zip(parent.values(), parent.keys()))
        for u, v in zip(parent.values(), parent.keys()):
            if (u, v) in G.edges():
                f[(u, v)] += min_flow
            else:
                f[(v, u)] -= min_flow
    
    return f
    

def main2(G, nodes):
    max_flow = ford_fulkerson_mine(G, 0, nodes[-1][-1])
    flow_value, flow_dict = nx.algorithms.flow.maximum_flow(G, 0, nodes[-1][-1])
    print(max_flow)
    print(flow_dict)