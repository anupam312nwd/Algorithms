#!/usr/bin/env python

from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


class object:
    def __init__(self, value, parent, rank):
        self.value = value
        self.parent = parent
        self.rank = rank

    def __str__(self):
        return f"value: {self.value}, parent: {self.parent}, rank: {self.rank}"


class unionByRank:
    def __init__(self, lists):
        self.dct = dict()
        for value in lists:
            self.dct[value] = object(value=value, parent=value, rank=1)

    def find(self, value):
        while self.dct[value].parent != value:
            value = self.dct[value].parent
        return value

    def union(self, val1, val2):
        root1 = self.find(val1)
        root2 = self.find(val2)
        if self.dct[root1].rank > self.dct[root2].rank:
            self.dct[root2].parent = root1
        elif self.dct[root1].rank < self.dct[root2].rank:
            self.dct[root1].parent = root2
        else:
            self.dct[root1].parent = root2
            self.dct[root2].rank += 1

    def connected(self, val1, val2):
        return self.find(val1) == self.find(val2)


if __name__ == "__main__":
    lst = [5, 6, "b", 2, 33, 7, 8]
    ubr = unionByRank(lists=lst)
    print(ubr.find("b"))
    print(ubr.dct["b"].rank, ubr.dct["b"].parent)
    ubr.union(2, 33)
    ubr.union(2, 5)
    ubr.union("b", 7)
    print(ubr.connected(2, 5))
    print(ubr.connected(7, "b"))
    print(ubr.connected(7, 8))
    # ubr.union(2, 7)
    # ubr.union(6, 8)
    ubr.union(6, 33)
    print("--------------------------------------------------")
    graph = defaultdict(list)
    for value in lst:
        print(ubr.dct[value])
        graph[value].append(ubr.dct[value].parent)
    G = nx.DiGraph(graph)
    # nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True)
    nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True, arrowsize=20)
    plt.savefig("nx_graph.png")
    print("code-ended!")
