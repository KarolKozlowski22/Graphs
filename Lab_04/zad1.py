import networkx as nx
import matplotlib.pyplot as plt
import random

def directed_graph(n, p):
    graph = []
    for i in range(n):
        graph.append([])
        for j in range(n):
            if i != j:
                rand = random.random()
                if rand < p:
                    graph[i].append(j)
        graph[i] = tuple(graph[i])
    print(graph)
    return graph

def draw(G, n):
    graph = nx.DiGraph()
    for i in range(n):
        for j in G[i]:
            graph.add_edge(i,j)
    nx.draw(graph, with_labels=True, font_weight='bold')
    filename = "graph"+ ".png"
    plt.savefig(filename)
    # plt.show()
    plt.close()


if __name__ == "__main__":
    G = directed_graph(9, 0.3)
    draw(G, 5 )