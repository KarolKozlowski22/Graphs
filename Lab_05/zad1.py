import networkx as nx
import matplotlib.pyplot as plt
import random

def graph_creation(N):
    nodes_per_cluster = []
    nodes_per_cluster.append(1)
    for _ in range(N):
        nodes_per_cluster.append(random.randrange(2,N+1))
    nodes_per_cluster.append(1)
    k=0
    nodes=[]
    for i in range(len(nodes_per_cluster)):
        nodes.append([])
        for _ in range(nodes_per_cluster[i]):
            nodes[i].append(k)
            k+=1
    
    G = nx.DiGraph()
    for i in range(len(nodes)):
        for j in nodes[i]:
            if j == 0:
                G.add_node(j, layer=i, label="Source")
            elif j == sum(nodes_per_cluster)-1:
                G.add_node(j, layer=i, label="Sink")
            G.add_node(j, layer=i)

    for i in range(len(nodes)-1):
        nodes_number_now = len(nodes[i])
        nodes_number_next = len(nodes[i+1])
        min_number = min(nodes_number_now, nodes_number_next)
        max_number = max(nodes_number_now, nodes_number_next)
        for number in range(0, min_number):
            while True:
                choosen_node = random.randrange(0,nodes_number_next)
                if G.degree[nodes[i+1][choosen_node]] == 0: 
                    G.add_weighted_edges_from([(nodes[i][number], nodes[i+1][choosen_node],random.randrange(1,11))])
                    break
        for number in range(min_number, max_number):
            if nodes_number_now >= nodes_number_next:
                choosen_node_now = 0
                for k in range(len(nodes[i])):
                    if G.out_degree[nodes[i][k]] == 0:
                        choosen_node_now = k
                choosen_node = random.randrange(0,nodes_number_next)
                G.add_weighted_edges_from([(nodes[i][choosen_node_now], nodes[i+1][choosen_node],random.randrange(1,11))])
            else:
                choosen_node_now = 0
                for k in range(len(nodes[i+1])):
                    if G.in_degree[nodes[i+1][k]] == 0:
                        choosen_node_now = k
                choosen_node = random.randrange(0,nodes_number_now)
                G.add_weighted_edges_from([(nodes[i][choosen_node], nodes[i+1][choosen_node_now],random.randrange(1,11))])
            
    return G, nodes

def add_edges(G, N, nodes):
    edges_to_add = 2*N
    for _ in range(edges_to_add):
        while True:    
            choosen_cluster = random.randrange(1,N+1)
            choosen_node_from = random.randrange(0,len(nodes[choosen_cluster]))
            choosen_node_to = random.randrange(0,len(nodes[choosen_cluster]) + len(nodes[choosen_cluster+1]))
            extra_add = 0
            if choosen_node_from == choosen_node_to:
                continue
            if choosen_node_to >= len(nodes[choosen_cluster]):
                extra_add = 1
                choosen_node_to -= len(nodes[choosen_cluster])
            if not G.has_edge(nodes[choosen_cluster][choosen_node_from], nodes[choosen_cluster+extra_add][choosen_node_to]) and not G.has_edge(nodes[choosen_cluster+extra_add][choosen_node_to], nodes[choosen_cluster][choosen_node_from]):
                G.add_weighted_edges_from([(nodes[choosen_cluster][choosen_node_from], nodes[choosen_cluster+extra_add][choosen_node_to], random.randrange(1,11))])
                break

def graph_visualization(G, nodes):
    positions = {}
    for i in range(len(nodes)):
        for j in range(len(nodes[i])):
            positions[nodes[i][j]] = (i*2,j*(-2))
    nx.draw_networkx(G, positions)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, positions, labels, label_pos=0.6)
    plt.show()

def main():
    N = 5
    G, nodes = graph_creation(N)
    add_edges(G, N, nodes)
    graph_visualization(G, nodes)

if __name__ == "__main__":
    main()