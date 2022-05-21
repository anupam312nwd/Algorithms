#!/usr/bin/env python

from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def bfs_que(graph, u):
    que = deque([u])
    lst = [u]
    visited = set(u)
    while que:
        v = que.popleft()
        for nbr in graph[v]:
            if nbr not in visited:
                que.append(nbr)
                visited.add(nbr)
                lst.append(nbr)
    return lst


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["D"],
        "D": ["F"],
        "E": ["D"],
        "F": [],
    }

    G = nx.from_dict_of_lists(graph)
    nx.draw_networkx(G, node_color="w", edgecolors="k")
    plt.savefig("graph.png")
    lst = bfs_que(graph, "A")
    print(lst)
