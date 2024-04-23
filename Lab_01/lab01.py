from converter_tests import *
from graph import Graph
import sys
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("--caltam", action="store_true", help="Test convert adjacency list to adjacency matrix function")
    parser.add_argument("--camtal", action="store_true", help="Test convert adjacency matrix to adjacency list function")
    parser.add_argument("--caltim", action="store_true", help="Test convert adjacency list to incidence matrix function")
    parser.add_argument("--cimtal", action="store_true", help="Test convert incidence matrix to adjacency list function")
    parser.add_argument("--camtim", action="store_true", help="Test convert adjacency matrix to incidence matrix function")
    parser.add_argument("--cimtam", action="store_true", help="Test convert incidence matrix to adjacency matrix function")
    parser.add_argument("-a", "--all", action="store_true", help="Run all tests")
    parser.add_argument("-f", "--file", nargs=2, help="Import graph from file")
    parser.add_argument("-d", "--draw", action="store_true", help="Draw graph from imported file")
    parser.add_argument("-r", "--random", action="store_true", help="Generate random graph")
    parser.add_argument("-s", "--save", action="store_true", help="Save generated graph to file")
    parser.add_argument("-h", "--help", action="store_true", help="Display this help and exit")

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(0)

    if args.all:
        convert_adjacency_list_to_adjacency_matrix_test()
        convert_adjacency_matrix_to_adjacency_list_test()
        convert_adjacency_list_to_incidence_matrix_test()
        convert_incidence_matrix_to_adjacency_list_test()
        convert_adjacency_matrix_to_incidence_matrix_test()
        convert_incidence_matrix_to_adjacency_matrix_test()
        sys.exit(0)

    if args.caltam:
        convert_adjacency_list_to_adjacency_matrix_test()
        sys.exit(0)

    if args.camtal:
        convert_adjacency_matrix_to_adjacency_list_test()
        sys.exit(0)

    if args.caltim:
        convert_adjacency_list_to_incidence_matrix_test()
        sys.exit(0)

    if args.cimtal:
        convert_incidence_matrix_to_adjacency_list_test()
        sys.exit(0)

    if args.camtim:
        convert_adjacency_matrix_to_incidence_matrix_test()
        sys.exit(0)

    if args.cimtam:
        convert_incidence_matrix_to_adjacency_matrix_test()
        sys.exit(0)

    if args.file:
        graph = Graph(args.file[0], args.file[1])
        if args.draw:
            graph.plot()
        else:
            raise ValueError("No action specified")
        sys.exit(0)

    # if args.random:
    #     graph = RandomGraph()
    #     if args.save:
    #         graph.save()
    #     if args.draw:
    #         graph.draw()
    #     sys.exit(0)

if __name__ == "__main__":
    main()
