#!/usr/bin/env python

from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

# from networkx.dr

plt.figure(figsize=(12, 12))


class Node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":

    nodes = [Node(0)] * 7
    nodes = [Node(-1)] * 7
    for i in range(1, 6):
        nodes[i] = Node(i)
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]

    root = nodes[1]

    graph = defaultdict(list)
    for i in range(1, 6):
        if nodes[i].left is not None:
            graph[i].append(nodes[i].left.val)
        if nodes[i].right is not None:
            graph[i].append(nodes[i].right.val)
    G = nx.DiGraph(graph)
    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")
    nx.draw_networkx(G, pos, edgecolors="k", node_color="w", arrows=True, arrowsize=20)

    # fmt: off
    # nx.draw(G, pos, with_labels=True, edgecolors="k", node_color="w", arrows=True, arrowsize=20,)
    # fmt: on

    plt.savefig("nx_graph.png")
    print("code-ended!")
