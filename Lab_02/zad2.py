from random import choice
from zad1 import draw, G


def randomize_graph(G):
    while True:
        first_edge = choice(list(G.edges()))
        second_edge = choice(list(G.edges()))
        while second_edge[0] in first_edge or second_edge[1] in first_edge:
            second_edge = choice(list(G.edges()))
        new_first = (min(first_edge[0], second_edge[0]), max(first_edge[0], second_edge[0]))
        new_second = (min(first_edge[1], second_edge[1]), max(first_edge[1], second_edge[1]))

        if new_first in list(G.edges()) or new_second in list(G.edges()):
            continue
        else:
            break
    G.remove_edge(*first_edge)
    G.remove_edge(*second_edge)
    G.add_edge(*new_first)
    G.add_edge(*new_second)
    return G



draw(randomize_graph(G))
