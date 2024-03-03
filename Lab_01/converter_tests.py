from converter import *
import numpy as np


def convert_adjacency_list_to_adjacency_matrix_test():
    print("Convert adjacency matrix to adjacency list")
    with open("adjacency_matrix", "r") as file_with_adjacency_matrix:
        adjacency_matrix = [[int(num) for num in line.split()] for line in file_with_adjacency_matrix]
        print("Adjacency matrix:")
        for row in adjacency_matrix:
            print(row)
        print("Adjacency list:")
        result = convert_adjacency_matrix_to_adjacency_list(adjacency_matrix)
        for ind, row in enumerate(result):
            print(f"{ind + 1}. " + "".join(str(row)))
        print("Matrix represents same graph as the list:", adjacency_matrix == convert_adjacency_list_to_adjacency_matrix(result))
        with open("adjacency_list", "r") as file_with_adjacency_list:
            expected_result = [[int(num) for num in line.split()] for line in file_with_adjacency_list]
            print("Expected result:")
            for ind, row in enumerate(expected_result):
                print(f"{ind + 1}. " + "".join(str(row)))
            print("Result coincides with expected result:", result == expected_result)


def convert_adjacency_matrix_to_adjacency_list_test():
    print("Convert adjacency list to adjacency matrix")
    with open("adjacency_list", "r") as file_with_adjacency_list:
        adjacency_list = [[int(num) for num in line.split()] for line in file_with_adjacency_list]
        print("Adjacency list:")
        for ind, row in enumerate(adjacency_list):
            print(f"{ind + 1}. " + "".join(str(row)))
        print("Adjacency matrix:")
        result = convert_adjacency_list_to_adjacency_matrix(adjacency_list)
        for row in result:
            print(row)
        print("List is the same as matrix:", adjacency_list == convert_adjacency_matrix_to_adjacency_list(result))
        with open("adjacency_matrix", "r") as file_with_adjacency_matrix:
            expected_result = [[int(num) for num in line.split()] for line in file_with_adjacency_matrix]
            print("Expected result:")
            for row in expected_result:
                print(row)
            print("Result coincides with expected result:", result == expected_result)


def convert_adjacency_list_to_incidence_matrix_test():
    print("Convert adjacency list to incidence matrix")
    with open("adjacency_list", "r") as file_with_adjacency_list:
        adjacency_list = [[int(num) for num in line.split()] for line in file_with_adjacency_list]
        print("Adjacency list:")
        for ind, row in enumerate(adjacency_list):
            print(f"{ind + 1}. " + "".join(str(row)))
        print("Incidence matrix:")
        result = convert_adjacency_list_to_incidence_matrix(adjacency_list)
        for row in result:
            print(row)
        print("List is the same as matrix:", adjacency_list == convert_incidence_matrix_to_adjacency_list(result))
        with open("incidence_matrix", "r") as file_with_incidence_matrix:
            expected_result = [[int(num) for num in line.split()] for line in file_with_incidence_matrix]
            print("Expected result:")
            for row in expected_result:
                print(row)
            expected_result_T = np.transpose(expected_result)
            result_T = np.transpose(result)
            for column in expected_result_T:
                if column not in result_T:
                    print("Result does not coincide with expected result")
                    return None
            else:
                print("Result coincides with expected result:", True)


def convert_incidence_matrix_to_adjacency_list_test():
    print("Convert incidence matrix to adjacency list")
    with open("incidence_matrix", "r") as file_with_incidence_matrix:
        incidence_matrix = [[int(num) for num in line.split()] for line in file_with_incidence_matrix]
        print("Incidence matrix:")
        for row in incidence_matrix:
            print(row)
        print("Adjacency list:")
        result = convert_incidence_matrix_to_adjacency_list(incidence_matrix)
        for ind, row in enumerate(result):
            print(f"{ind + 1}. " + "".join(str(row)))
        incidence_matrix_T = np.transpose(incidence_matrix)
        reversed_result_T = np.transpose(convert_adjacency_list_to_incidence_matrix(result))
        for column in incidence_matrix_T:
            if column not in reversed_result_T:
                print("Result does not coincide with expected result")
                return None
        else:
            print("Result coincides with expected result:", True)
        with open("adjacency_list", "r") as file_with_adjacency_list:
            expected_result = [[int(num) for num in line.split()] for line in file_with_adjacency_list]
            print("Expected result:")
            for ind, row in enumerate(result):
                print(f"{ind + 1}. " + "".join(str(row)))
            print("Result coincides with expected result:", result == expected_result)


def convert_adjacency_matrix_to_incidence_matrix_test():
    print("Convert adjacency matrix to incidence matrix")
    with open("adjacency_matrix", "r") as file_with_adjacency_matrix:
        adjacency_matrix = [[int(num) for num in line.split()] for line in file_with_adjacency_matrix]
        print("Adjacency matrix:")
        for row in adjacency_matrix:
            print(row)
        print("Incidence matrix:")
        result = convert_adjacency_matrix_to_incidence_matrix(adjacency_matrix)
        for row in result:
            print(row)
        print("Matrix represents same graph as the list:", adjacency_matrix == convert_incidence_matrix_to_adjacency_matrix(result))
        with open("incidence_matrix", "r") as file_with_incidence_matrix:
            expected_result = [[int(num) for num in line.split()] for line in file_with_incidence_matrix]
            print("Expected result:")
            for row in expected_result:
                print(row)
            expected_result_T = np.transpose(expected_result)
            result_T = np.transpose(result)
            for column in expected_result_T:
                if column not in result_T:
                    print("Result does not coincide with expected result")
                    return None
            else:
                print("Result coincides with expected result:", True)


def convert_incidence_matrix_to_adjacency_matrix_test():
    print("Convert incidence matrix to adjacency matrix")
    with open("incidence_matrix", "r") as file_with_incidence_matrix:
        incidence_matrix = [[int(num) for num in line.split()] for line in file_with_incidence_matrix]
        print("Incidence matrix:")
        for row in incidence_matrix:
            print(row)
        print("Adjacency matrix:")
        result = convert_incidence_matrix_to_adjacency_matrix(incidence_matrix)
        for row in result:
            print(row)
        incidence_matrix_T = np.transpose(incidence_matrix)
        reversed_result_T = np.transpose(convert_adjacency_matrix_to_incidence_matrix(result))
        for column in incidence_matrix_T:
            if column not in reversed_result_T:
                print("Result does not coincide with expected result")
                return None
        else:
            print("Result coincides with expected result:", True)
        with open("adjacency_matrix", "r") as file_with_adjacency_matrix:
            expected_result = [[int(num) for num in line.split()] for line in file_with_adjacency_matrix]
            print("Expected result:")
            for row in expected_result:
                print(row)
            print("Result coincides with expected result:", result == expected_result)
