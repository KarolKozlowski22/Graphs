import numpy as np
import matplotlib.pyplot as plt

from Lab_01.import_graph import ImportGraph


def draw_graph(graph):
    num_nodes = len(graph)

    theta = np.linspace(0, 2*np.pi, num_nodes, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    plt.scatter(x, y, c='skyblue', s=630, edgecolors='black', zorder=2)
    print(num_nodes)
    for i in range(num_nodes):
        plt.text(x[i], y[i], str(i + 1), color='black', fontsize=10, ha='center', va='center', zorder=3)

    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            plt.plot([x[node], x[neighbor - 1]], [y[node], y[neighbor - 1]], color='black', linewidth=1, zorder=1)

    plt.axis('equal')
    plt.axis('off')
    plt.show()

    # tescik
    # file_path = "adjacency_list"
    # graph_representation = "AL"
    #
    # graph = ImportGraph(graph_representation, file_path)
    # adjacency_list = list(graph)
    #
    # draw_graph(adjacency_list)


