from random import choice
import copy
from zad1 import draw, G
# import networkx as nx

def randomize_graph(G):
    first_edge=choice(list(G.edges()))
    print(*first_edge)
    second_edge=choice(list(G.edges()))
    while second_edge[0] in first_edge or second_edge[1] in first_edge:
        second_edge=choice(list(G.edges()))
    G.remove_edge(*second_edge)
    G.add_edge(first_edge[0],second_edge[0])
    G.add_edge(first_edge[1],second_edge[1])
    return G

# def randomize_graphs(G):
#     G_copy=copy.deepcopy(G)
#     while not nx.is_connected(G_copy):
#         G_copy=randomize_graph(G_copy)
#     return G_copy

draw(randomize_graph(G))

    



