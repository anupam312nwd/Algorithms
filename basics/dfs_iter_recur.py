from collections import deque

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.drawing.nx_agraph import graphviz_layout


def dfs_iterative(graph, root):
    """using stack data structure"""
    stack = [root]
    visited = set([root])
    visited_in_order = []
    appended = False

    while stack:
        for nbr in graph[stack[-1]]:
            if nbr not in visited:
                appended = True
                visited.add(nbr)
                stack.append(nbr)
        if not appended:
            visited_in_order.append(stack.pop())
    visited_in_order.reverse()
    return visited_in_order


def dfs_recursive(graph, root, visited_in_order=None, visited=None):
    """stack data structure not needed"""
    if visited is None:
        visited = set([root])
    if visited_in_order is None:
        visited_in_order = [root]
    for nbr in np.random.permutation(graph[root]):
        if nbr not in visited:
            visited.add(nbr)
            visited_in_order.append(nbr)
            dfs_recursive(graph, nbr, visited_in_order, visited=visited)
    return visited_in_order


if __name__ == "__main__":

    graph = {1: [2, 5], 2: [3, 4]}
    graph = {
        "a": ["b", "c"],
        "b": ["d", "f", "g"],
        "c": ["d"],
        "d": ["e"],
        "e": ["g"],
        "f": ["h"],
        "g": ["f", "h"],
        "h": [],
    }

    print(dfs_iterative(graph, "a"))
    print(dfs_recursive(graph, "a"))
    G = nx.from_dict_of_lists(graph)
    pos = graphviz_layout(G, prog="dot")
    nx.draw(G, pos=pos, with_labels=True, arrows=True)
    plt.show()
