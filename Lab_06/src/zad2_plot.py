import matplotlib.pyplot as plt

def read_result_file(filename):
    nodes=[]
    with open(filename, "r") as file:
        for line in file.readlines():
            nodes.append(tuple(line.strip().split(" ")))

    nodes = list(map(lambda x: (int(x[0]), int(x[1])), nodes))
    return nodes


def plot_cycle(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    
    plt.figure(figsize=(10, 10))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    plt.title('Najkrótszy znaleziony cykl')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

nodes = read_result_file('result.txt')

plot_cycle(nodes)