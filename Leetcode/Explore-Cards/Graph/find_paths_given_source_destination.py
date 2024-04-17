#!/usr/bin/env python

## https://www.geeksforgeeks.org/find-paths-given-source-destination/

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


def all_paths_between_two_vertices(src, target, graph):
    all_paths = []
    visited = set()

    def dfs(current, target, path, graph):
        visited.add(current)
        path.append(current)
        if current == target:
            all_paths.append(path.copy())
        else:
            for nbr in graph[current]:
                if nbr not in visited:
                    dfs(nbr, target, path, graph)
        path.pop()
        visited.remove(current)

    dfs(src, target, [], graph)
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
