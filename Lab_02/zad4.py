import networkx as nx
from networkx import is_eulerian
from zad1 import draw
import random 


def create_eulerian_graph(n):
    G=nx.Graph()
    if n % 2 != 0:
        raise ValueError("Liczba wierzchołków musi być parzysta, aby stworzyć graf eulerowski")
    
    adj_list = {i: [(i + 1) % n, (i - 1 + n) % n] for i in range(n)}
    
    if n > 2:
        for i in range(n):
            for j in range(2, n // 2):
                adj_list[i].append((i + j) % n)
                adj_list[i].append((i - j + n) % n)
    
    for key in adj_list:
        adj_list[key] = list(set(adj_list[key]))

    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            G.add_edge(i, adj_list[i][j])

    return G

def fleurys_algorithm(graph):
    current_node = 0
    neighbors = list(graph.neighbors(current_node))
    next_node = neighbors.pop()
    euler_cycle = [current_node]

    while graph.has_edge(current_node, next_node):
        euler_cycle.append(next_node)
        graph.remove_edge(current_node, next_node)

        if graph.number_of_edges() == 0:
            break

        current_node = next_node
        neighbors = list(graph.neighbors(current_node))
        next_node = neighbors.pop()

    return euler_cycle


n=random.randint(3,20)
while n%2!=0:
    n=random.randint(3,20)

# for i in range(20):
G=create_eulerian_graph(n)
draw(G)
if is_eulerian(G):
    print("Graf jest eulerowski")
else:
    print("Graf nie jest eulerowski")
    # break

euler_cycle = fleurys_algorithm(G)
print(euler_cycle)


