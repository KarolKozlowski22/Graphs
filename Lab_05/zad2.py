import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque
from zad1 import graph_visualization

def ford_fulkerson_mine(G, s, t):
    def cf(u, v):
        if (u, v) in G.edges():
            return G[u][v]['capacity'] - f[(u, v)]
        if (v, u) in G.edges():
            return f[(v, u)]
        else:
            return 0
    
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
                        ps = dict(reversed(list(ps.items())))
                        ps_true = {}
                        k = t
                        while True:
                            ps_true[k] = ps[k]
                            k = ps[k]
                            if k == 0:
                                break
                        return True, ds, ps_true
        return False, ds, ps
    
    def build_residual_network(G, f):
        Gf = nx.DiGraph()
        for n in G.nodes():
            Gf.add_node(n)
        for (u, v) in G.edges():
            if f[(u, v)] == 0:
                Gf.add_edge(u, v, capacity=G[u][v]['capacity'])
            elif f[(u, v)] == G[u][v]['capacity']:
                Gf.add_edge(v, u, capacity=G[u][v]['capacity'])
            else:
                Gf.add_edge(u, v, capacity=(G[u][v]['capacity'] - f[(u, v)]))
                Gf.add_edge(v, u, capacity=f[(u, v)])
        return Gf

    f = {(u, v): 0 for u, v in G.edges()}

    while True:
        Gf = build_residual_network(G, f)
        path_exists, ds, parent = bfs(Gf, s, t)
        if not path_exists:
            break
        min_flow = min(cf(u, v) for u, v in zip(parent.values(), parent.keys()))
        for u, v in zip(parent.values(), parent.keys()):
            if (u, v) in G.edges():
                f[(u, v)] += min_flow
            else:
                f[(v, u)] -= min_flow
    
    fmax = 0
    for u in G[0]:
        fmax += f[(0,u)]
    return f, fmax

def graph_visualization_2(G, nodes, max_flow):
    for u, v in max_flow:
        G[u][v]['capacity'] = str(max_flow[(u, v)]) + '/' + str(G[u][v]['capacity'])
    graph_visualization(G, nodes, 'zad2.png')
    

def main2(G, nodes):
    flow, max_flow = ford_fulkerson_mine(G, 0, nodes[-1][-1])
    print('Maksymalny przeplyw: ', max_flow)
    graph_visualization_2(G, nodes, flow)