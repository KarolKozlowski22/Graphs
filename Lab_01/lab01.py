from converter_tests import *
from graph import Graph, RandomGraph
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description="Graph representation converter", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Display this manual")
    parser.add_argument("--caltam", action="store_true", help="Test convert adjacency list to adjacency matrix function")
    parser.add_argument("--camtal", action="store_true", help="Test convert adjacency matrix to adjacency list function")
    parser.add_argument("--caltim", action="store_true", help="Test convert adjacency list to incidence matrix function")
    parser.add_argument("--cimtal", action="store_true", help="Test convert incidence matrix to adjacency list function")
    parser.add_argument("--camtim", action="store_true", help="Test convert adjacency matrix to incidence matrix function")
    parser.add_argument("--cimtam", action="store_true", help="Test convert incidence matrix to adjacency matrix function")
    parser.add_argument("-a", "--all", action="store_true", help="Run all tests")
    parser.add_argument("-f", "--file", nargs=2, help="Import graph from file")
    parser.add_argument("-d", "--draw", action="store_true", help="Draw graph from imported file")
    parser.add_argument("-r", "--random", nargs="+", help="Generate random graph [NUM_NODES] [p PROBABILITY] else random number of nodes and edges without probability")
    parser.add_argument("-s", "--save", action="store_true", help="Save generated graph to file")
    parser.add_argument("-sp", "--save_plot", action="store_true", help="Save plot to file")

    args = parser.parse_args()

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
            if args.save_plot:
                graph.plot(save=True)
            else:
                graph.plot()
        else:
            raise ValueError("No action specified")
        sys.exit(0)

    if args.random:
        if args.random is not True:
            if len(args.random) == 1:
                if int(args.random[0]) < 1:
                    raise ValueError("Invalid number of nodes")
                graph = RandomGraph(int(args.random[0]))
            elif len(args.random) == 2:
                if args.random[0] == "p":
                    if 0 <= float(args.random[1]) < 1:
                        graph = RandomGraph(probability=float(args.random[1]))
                    else:
                        raise ValueError("Invalid probability")
            elif len(args.random) == 3:
                if args.random[1] == "p":
                    if 0 <= float(args.random[2]) < 1:
                        if int(args.random[0]) < 1:
                            raise ValueError("Invalid number of nodes")
                        graph = RandomGraph(int(args.random[0]), float(args.random[2]))
                    else:
                        raise ValueError("Invalid probability")
            else:
                raise ValueError("Invalid arguments")
        else:
            graph = RandomGraph()
        if args.save:
            graph.save()
        if args.draw:
            if args.save_plot:
                graph.plot(save=True)
            else:
                graph.plot()
        else:
            print(graph)
        sys.exit(0)

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
