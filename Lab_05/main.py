import networkx as nx
import matplotlib.pyplot as plt
import random
from zad1 import main1
from zad2 import main2

G = nx.DiGraph()
N = 4
nodes=[]

main1(G, N, nodes)
main2(G, nodes)