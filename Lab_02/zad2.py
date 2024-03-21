from random import choice
# import copy
from zad1 import draw, G


def randomize_graph(G):
    print(G.edges())
    while True:
        first_edge = choice(list(G.edges()))
        print(*first_edge)
        while True:
            second_edge = choice(list(G.edges()))
            if second_edge[0] == first_edge[0] or second_edge[0] == first_edge[1] or second_edge[1] == first_edge[1] or second_edge[1] == first_edge[0]:
                continue
            else:
                break
        print(*second_edge)
        G.remove_edge(*second_edge)
        G.remove_edge(*first_edge)
        while second_edge[0] in first_edge or second_edge[1] in first_edge:
            second_edge = choice(list(G.edges()))

        new_first = (first_edge[0], first_edge[1])
        new_second = (second_edge[0], second_edge[1])
        if new_first in list(G.edges()) or new_second in list(G.edges()):
            continue
        else:
            break

    print(first_edge[0], second_edge[0])
    print(first_edge[1], second_edge[1])
    G.add_edge(first_edge[0], second_edge[0])
    G.add_edge(first_edge[1], second_edge[1])
    return G


draw(randomize_graph(G))
