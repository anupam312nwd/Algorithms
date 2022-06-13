#!/usr/bin/env python

## https://www.geeksforgeeks.org/find-paths-given-source-destination/

import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


def all_paths_between_two_vertices(src, dst, graph):
    all_paths = []

    def helper(src: str, dst: str, visited: dict, path: list, graph):
        visited[src] = True
        path.append(src)
        if src == dst:
            all_paths.append(path.copy())
        else:
            for nbr in graph[src]:
                if visited[nbr] == False:
                    helper(nbr, dst, visited, path, graph)
        path.pop()
        visited[src] = False

    visited = {v: False for v in graph}
    helper(src, dst, visited, [], graph)
    return all_paths


if __name__ == "__main__":
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
    all_paths = all_paths_between_two_vertices("a", "g", graph)
    print(all_paths)
    # G = nx.DiGraph(graph)
    # nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True, arrowsize=20)
    # plt.savefig("nx_graph.png")
    print("code-ended!")
