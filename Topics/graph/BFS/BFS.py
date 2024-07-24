from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


def bfs_iterative(graph, root):
    """using queue data structure"""
    que = deque([root])
    visited = [root]
    while que:
        popped = que.pop()
        for nbr in graph[popped]:
            if nbr not in visited:
                visited.append(nbr)
                que.appendleft(nbr)
    return visited


def bfs_recursive(graph, root, visited_in_order=None, visited=None):
    if visited is None:
        visited = set([root])
    if visited_in_order is None:
        visited_in_order = [root]
    for nbr in graph[root]:
        visited_nbr = []
        if nbr not in visited:
            visited.add(nbr)
            visited_nbr.append(nbr)
        visited_in_order += visited_nbr
        for nbr in visited_nbr:
            bfs_recursive(graph, nbr, visited_in_order, visited)
    return visited_in_order


if __name__ == "__main__":

    graph = {
        "a": ["b", "d", "c"],
        "b": ["a", "d", "e"],
        "c": ["a", "i"],
        "d": ["a", "b", "h"],
        "e": ["b"],
        "h": ["d", "i"],
        "i": ["h", "k"],
        "k": ["i"],
    }

    print(bfs_iterative(graph, "a"))
    print(bfs_recursive(graph, "a"))
    G = nx.from_dict_of_lists(graph)
    G = nx.Graph(graph)
    nx.draw(
        G,
        node_color="white",
        arrowstyle="-|>",
        edgecolors="black",
        with_labels=True,
        arrows=True,
    )
    # nx.draw_spring(G)
    # nx.draw_networkx(G)
    # nx.draw(G)
    plt.savefig("graph.png")
