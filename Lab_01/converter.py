from typing import List


def convert_adjacency_list_to_adjacency_matrix(adjacency_list: List[List[int]]) -> List[List[int]]:
    adjacency_matrix = [[0 for _ in range(len(adjacency_list))] for _ in range(len(adjacency_list))]
    for row in range(len(adjacency_list)):
        for column in adjacency_list[row]:
            adjacency_matrix[row][column - 1] = 1
    return adjacency_matrix


def convert_adjacency_matrix_to_adjacency_list(adjacency_matrix: List[List[int]]) -> List[List[int]]:
    adjacency_list = [[] for _ in range(len(adjacency_matrix))]
    for column in range(len(adjacency_matrix[0])):
        for row in range(len(adjacency_matrix)):
            if adjacency_matrix[row][column] == 1:
                adjacency_list[row].append(column + 1)
    return adjacency_list


def convert_adjacency_matrix_to_incidence_matrix(adjacency_matrix: List[List[int]]) -> List[List[int]]:
    edges = sum([sum(row) for row in adjacency_matrix]) // 2
    incidence_matrix = [[0 for _ in range(edges)] for _ in range(len(adjacency_matrix))]
    edge = 0
    for row in range(len(adjacency_matrix)):
        for column in range(row + 1, len(adjacency_matrix)):
            if adjacency_matrix[row][column] == 1:
                incidence_matrix[row][edge] = incidence_matrix[column][edge] = 1
                edge += 1
    return incidence_matrix


def convert_incidence_matrix_to_adjacency_matrix(incidence_matrix: List[List[int]]) -> List[List[int]]:
    adjacency_matrix = [[0 for _ in range(len(incidence_matrix))] for _ in range(len(incidence_matrix))]
    for i in range(len(incidence_matrix[0])):
        for j in range(len(incidence_matrix)):
            if incidence_matrix[j][i] == 1:
                for k in range(j + 1, len(incidence_matrix)):
                    if incidence_matrix[k][i] == 1:
                        adjacency_matrix[j][k] = adjacency_matrix[k][j] = 1
    return adjacency_matrix


def convert_adjacency_list_to_incidence_matrix(adjacency_list: List[List[int]]) -> List[List[int]]:
    return convert_adjacency_matrix_to_incidence_matrix(convert_adjacency_list_to_adjacency_matrix(adjacency_list))


def convert_incidence_matrix_to_adjacency_list(incidence_matrix: List[List[int]]) -> List[List[int]]:
    return convert_adjacency_matrix_to_adjacency_list(convert_incidence_matrix_to_adjacency_matrix(incidence_matrix))
