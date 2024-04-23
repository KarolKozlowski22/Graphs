import numpy as np
import matplotlib.pyplot as plt
from converter import convert_adjacency_matrix_to_adjacency_list, convert_incidence_matrix_to_adjacency_list


class Graph:
    def __init__(self, representation_type, file_path):
        self.file_path = file_path
        self.graph = []
        self.import_graph()
        self.representation_type = representation_type

    def import_graph(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.graph.append(list(map(int, line.split())))

    def __iter__(self):
        return iter(self.graph)

    def __str__(self):
        return str(self.graph)

    def plot(self):
        graph = self.graph
        if self.representation_type == "AM":
            graph = convert_adjacency_matrix_to_adjacency_list(self.graph)
        elif self.representation_type == "IM":
            graph = convert_incidence_matrix_to_adjacency_list(self.graph)
        num_nodes = len(graph)

        theta = np.linspace(0, 2*np.pi, num_nodes, endpoint=False)
        x = np.cos(theta)
        y = np.sin(theta)

        plt.figure(figsize=(8, 8))

        plt.scatter(x, y, c='skyblue', s=630, edgecolors='black', zorder=2)
        for i in range(num_nodes):
            plt.text(x[i], y[i], str(i + 1), color='black', fontsize=10, ha='center', va='center', zorder=3)

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                plt.plot([x[node], x[neighbor - 1]], [y[node], y[neighbor - 1]], color='black', linewidth=1, zorder=1)

        plt.axis('equal')
        plt.axis('off')
        plt.show()

    # TODO: Implement checking if provided representation type is valid with provided file