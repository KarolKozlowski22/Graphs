import numpy as np
import random

def generate_random_digraph(n,p):
    adj_matrix=np.zeros((n,n),dtype=int)
    for i in range(n):
        for j in range(n):
            if i!=j and random.random()<p:
                adj_matrix[i][j]=1
    return adj_matrix

def matrix_to_edge_list(adj_matrix):
    edges=[]

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j]==1:
                edges.append((i,j))

    return edges

n=5
p=0.3

print("Macierz sasiedztwa dla grafu z liczbą krawędzi {n} i maksymalną prawdopobieństwem istnietnia konkretnej krawędzi {p}")
adj_matrix=generate_random_digraph(n,p)
print(adj_matrix)
print("Lista wierzchołków uzyskana z macierzy sąsiedztwa")
edges=matrix_to_edge_list(adj_matrix)
print(edges)