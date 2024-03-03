class ImportGraph:
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

    # TODO: Implement checking if provided representation type is valid with provided file