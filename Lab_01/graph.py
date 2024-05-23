import matplotlib.pyplot as plt
import random
import networkx as nx
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

        G = nx.Graph()

        for node, neighbors in enumerate(graph):
            for neighbor, is_neighbor in enumerate(neighbors):
                if is_neighbor:
                    G.add_edge(node, neighbor)
            print(' ')

        pos = nx.circular_layout(G)

        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray', width=2)

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

