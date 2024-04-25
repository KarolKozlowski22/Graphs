from Lab_03.zad3 import gen_distance_matrix
from Lab_03.zad1 import gen_connected_graph_with_wages
from Lab_03.zad2 import dijkstra
from Lab_03.zad4 import get_centrum, get_centrum_minimax
from Lab_03.zad5 import prim, kruskal


def main():
    # Zadanie 1 - wygenerowanie grafu i nadanie wag krawedziom
    graph, w = gen_connected_graph_with_wages(7, 4)
    print("Zadanie 1.\n\nweight matrix: \n", w, "\n")

    # Zadanie 2 - algorytm dijkstry
    node = 0
    d, p = dijkstra(graph, w, node)
    print("Zadanie 2.\n\nnajkrotsze sciezki od wierzcholka ", node)
    print(d, "\n")

    # Zadanie 3 - macierz odleglosci
    distance_matrix = gen_distance_matrix(graph, w)
    print("Zadanie 3.\n\ndistance matrix:\n", distance_matrix, "\n")

    # Zadanie 4 - centrum i centrum minimax
    centrum = get_centrum(graph, w)
    centrum_minimax = get_centrum_minimax(graph, w)
    print("Zadanie 4.\n")
    print("centrum: ", centrum)
    print("centrum_minimax: ", centrum_minimax, "\n")

    # Zadanie 5 - Algorytmy Prima i Kruskala do znajdowania minimalnego drzewa rozpinajacego
    print("Zadanie 5.\n")
    prim_mst = prim(graph, 0)
    print("Prim's mst: ", prim_mst)
    kruskal_mst = kruskal(graph)
    print("Kruskal's mst: ", kruskal_mst)


if __name__ == "__main__":
    main()
