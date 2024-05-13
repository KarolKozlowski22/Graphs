import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
from zad1 import graph_visualization

def ford_fulkerson_mine(G, s, t):
    def cf(u, v):
        return G[u][v]['capacity'] - f[(u, v)]
    
    def bfs(Gf, s, t):
        Q = deque()
        Q.append(s)
        ds = {v: float('inf') for v in Gf}
        ds[s] = 0 
        ps = {}
        while Q:
            v = Q.popleft()
            for u in Gf[v]:
                if ds[u] == float('inf') and cf(v, u) > 0:
                    ds[u] = ds[v] + 1
                    ps[u] = v
                    Q.append(u)
                    if u == t:
                        return True, ds, ps
        return False, ds, ps
    
    f = {(u, v): 0 for u, v in G.edges()}

    while True:
        path_exists, ds, parent = bfs(G, s, t)
        if not path_exists:
            break
        min_flow = min(cf(u, v) for u, v in zip(parent.values(), parent.keys()))
        for u, v in zip(parent.values(), parent.keys()):
            if (u, v) in G.edges():
                f[(u, v)] += min_flow
            else:
                f[(v, u)] -= min_flow
    
    return f

def graph_visualization_2(G, nodes, max_flow):
    for u, v in max_flow:
        G[u][v]['capacity'] = str(max_flow[(u, v)]) + '/' + str(G[u][v]['capacity'])
    graph_visualization(G, nodes, 'zad2.png')
    

def main2(G, nodes):
    max_flow = ford_fulkerson_mine(G, 0, nodes[-1][-1])
    flow_value, flow_dict = nx.algorithms.flow.maximum_flow(G, 0, nodes[-1][-1])
    print(max_flow)
    print(flow_dict)
    graph_visualization_2(G, nodes, max_flow)