import copy
import networkx as nx
import matplotlib.pyplot as plt


def degree_seq(A):
    A_copy = copy.deepcopy(A)
    A_copy.sort(reverse=True)
    while True:
        if all(value == 0 for value in A_copy):
            return True
        if A[0] >= len(A_copy) or any(A_copy[i] < 0 for i in range(len(A_copy))):
            return False
        for i in range(1, A_copy[0] + 1):
            A_copy[i] -= 1
        A_copy[0] = 0
        A_copy.sort(reverse=True)


def create_graph(A):
    G = nx.Graph()

    if degree_seq(A):
        A.sort(reverse=True)
        G.add_nodes_from(range(len(A)))
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > 0 and A[j] > 0:
                    G.add_edge(i, j)
                    A[i] -= 1
                    A[j] -= 1
        return G
    else:
        return False


def draw(G):
    global counter
    if G:
        nx.draw_circular(G, with_labels=True, font_weight='bold')
        filename = "graph" + str(counter) + ".png"
        plt.savefig(filename)
        plt.close()
    else:
        print("Nie powstal graf poniewaz to nie byl ciag graficzny")
    counter += 1


counter = 1
A = [1, 3, 2, 3, 2, 4, 1]
# A = [4, 3, 3, 2, 2]
G = create_graph(A)
draw(G)
