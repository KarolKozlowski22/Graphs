from random import choice
# import copy
from zad1 import draw, G


def randomize_graph(G):
    first_edge = choice(list(G.edges()))
    print(*first_edge)
    second_edge = choice(list(G.edges()))
    print(*second_edge)
    while second_edge[0] in first_edge or second_edge[1] in first_edge:
        second_edge = choice(list(G.edges()))
    G.remove_edge(*second_edge)
    G.remove_edge(*first_edge)
    print(first_edge[0], second_edge[0])
    print(first_edge[1], second_edge[1])
    G.add_edge(first_edge[0], second_edge[0])
    G.add_edge(first_edge[1], second_edge[1])
    return G


draw(randomize_graph(G))
