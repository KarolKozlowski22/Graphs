import numpy as np
import matplotlib.pyplot as plt
import random
from converter import convert_adjacency_matrix_to_adjacency_list, convert_incidence_matrix_to_adjacency_list


class Graph:
    def __init__(self, representation_type, file_path):
        self.file_path = file_path
        self.graph = []
        self.import_graph()
        self.representation_type = representation_type

    def import_graph(self):
        if self.file_path is not None:
            with open(self.file_path, "r") as file:
                for line in file:
                    self.graph.append(list(map(int, line.split())))

    def __iter__(self):
        return iter(self.graph)

    def __str__(self):
        return str(self.graph)

    def plot(self, save=False):
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

        if save:
            plt.savefig("graph.png")
        else:
            plt.show()

    # TODO: Implement checking if provided representation type is valid with provided file


class RandomGraph(Graph):
    def __init__(self, num_nodes=random.randint(1, 10), probability=None):
        super().__init__('AL', None)
        self.num_nodes = num_nodes
        self.probability = probability
        self.graph = self.generate_random_graph()

    def generate_random_graph(self):
        graph = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if random.choice([True, False]) if self.probability is None else random.random() > self.probability:
                    graph[i][j] = graph[j][i] = 1
        return graph

    def save(self):
        with open("random_graph", "w") as file:
            for row in self.graph:
                file.write(" ".join(map(str, row)) + "\n")
