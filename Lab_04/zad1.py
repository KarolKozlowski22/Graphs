import networkx as nx
import matplotlib.pyplot as plt
import random


def directed_graph(n, p):
    graph = []
    for i in range(n):
        graph.append([]) # pusta lista sąsiedztwa dla wierzcholka
        for j in range(n):
            if i != j:
                rand = random.random()  # losowanie liczby z przedzialu 0, 1
                if rand < p: 
                    graph[i].append(j)   # dodanie krawedzi jesli wylosowana liczba jest mniejsza od p
        graph[i] = tuple(graph[i]) 
    return graph


def print_graph(graph):
    for i, el in enumerate(graph):
        print(f"{i}: {el}")


def draw(G):
    n = len(G)
    graph = nx.DiGraph() 
    for i in range(n):
        graph.add_node(i)
    for i in range(n):
        for j in G[i]:
            graph.add_edge(i, j)  # dodanie krawedzi z i do j
    pos = nx.spring_layout(graph) 
    nx.draw(graph, with_labels=True, font_weight="bold")
    filename = "graph" + ".png"
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    n = 5         #ilosc wierzcholkow
    p = 0.4      #prawdopodobienstwo 
    G = directed_graph(n, p)
    print_graph(G)      #wypisanie listy sasiedztwa
    draw(G)
