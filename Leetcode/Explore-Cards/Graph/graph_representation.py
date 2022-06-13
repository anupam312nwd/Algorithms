#!/usr/bin/env python

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


if __name__ == "__main__":
    edges = [
        [0, 7],
        [0, 8],
        [6, 1],
        [2, 0],
        [0, 4],
        [5, 8],
        [4, 7],
        [1, 3],
        [3, 5],
        [6, 5],
    ]
    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)
    print(graph.graph)
    G = nx.DiGraph(graph.graph)
    nx.draw_networkx(G)
    plt.savefig("nx_graph.png")
    print("code-ended!")
