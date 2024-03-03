from converter_tests import *
from import_graph import ImportGraph
import sys


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--caltam":
        convert_adjacency_list_to_adjacency_matrix_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "--camtal":
        convert_adjacency_matrix_to_adjacency_list_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "--caltim":
        convert_adjacency_list_to_incidence_matrix_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "--cimtal":
        convert_incidence_matrix_to_adjacency_list_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "--camtim":
        convert_adjacency_matrix_to_incidence_matrix_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "--cimtam":
        convert_incidence_matrix_to_adjacency_matrix_test()
    elif len(sys.argv) == 2 and sys.argv[1] == "-a" or sys.argv[1] == "--all":
        convert_adjacency_list_to_adjacency_matrix_test()
        convert_adjacency_matrix_to_adjacency_list_test()
        convert_adjacency_list_to_incidence_matrix_test()
        convert_incidence_matrix_to_adjacency_list_test()
        convert_adjacency_matrix_to_incidence_matrix_test()
        convert_incidence_matrix_to_adjacency_matrix_test()
    elif len(sys.argv) == 4 and sys.argv[1] == "-i" or sys.argv[1] == "--import":
        # Check if provided file exists
        try:
            with open(sys.argv[3], "r"):
                pass
        except FileNotFoundError:
            print("Error: File not found")
            return
        # Check if provided representation type is supported
        if sys.argv[2] not in ["AL", "AM", "IM"]:
            raise ValueError("Error: Invalid representation type"
                             " (AL - adjacency list, AM - adjacency matrix, IM - incidence matrix)")
        graph = ImportGraph(sys.argv[2], sys.argv[3])
        print("Graph imported from file:")
        for row in graph:
            print(row)
        # draw_graph(graph)
    elif len(sys.argv) == 2 and sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: python3 lab01.py [OPTION]")
        print("Options:")
        print("  --caltam   Test convert adjacency list to adjacency matrix function")
        print("  --camtal   Test convert adjacency matrix to_adjacency list function")
        print("  --caltim   Test convert adjacency list to incidence matrix function")
        print("  --cimtal   Test convert incidence matrix to adjacency list function")
        print("  --camtim   Test convert adjacency matrix to incidence matrix function")
        print("  --cimtam   Test convert incidence matrix to adjacency matrix function")
        print("  -a, --all  Run all tests")
        print("  -i, --import [REPRESENTATION_TYPE] [PATH_TO_FILE] Import graph from file")
        print("     supported representation types:")
        print("         AL - adjacency list")
        print("         AM - adjacency matrix")
        print("         IM - incidence matrix")
        print("  -d, --draw  Draw graph from imported file")
        print("  -r, --random   Generate random graph")
        print("  -h, --help Display this help and exit")
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
