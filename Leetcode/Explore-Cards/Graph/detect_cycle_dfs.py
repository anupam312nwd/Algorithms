#!/usr/bin/env python


import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


def detect_cycle_recur(v, graph):
    visited = set()
    path = set()

    def dfs(vertex, visited, visiting):
        if vertex in visiting:
            return True
        if vertex in visited:
            return False
        visited.add(vertex)
        visiting.add(vertex)
        for nbr in graph[vertex]:
            if dfs(nbr, visited, visiting):
                return True
        visiting.remove(vertex)
        return False

    return dfs(v, visited, path)


if __name__ == "__main__":
    graph_no_cycle = {"a": ["b", "c"], "b": ["e"], "c": ["b", "d"], "d": ["e"], "e": []}
    print(detect_cycle_recur("a", graph_no_cycle))

    graph_w_cycle = {"a": ["b", "c"], "b": ["e"], "c": ["b"], "d": ["c"], "e": ["d"]}
    print(detect_cycle_recur("a", graph_w_cycle))

    # G = nx.DiGraph(graph_no_cycle)
    # nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True, arrowsize=20)
    # plt.savefig("graph_no_cycle.png")
    # plt.clf()
    # G = nx.DiGraph(graph_w_cycle)
    # nx.draw_networkx(G, edgecolors="k", node_color="w", arrows=True, arrowsize=20)
    # plt.savefig("graph_w_cycle.png")
