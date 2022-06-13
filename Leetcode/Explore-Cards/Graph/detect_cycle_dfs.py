#!/usr/bin/env python


import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))


def detect_cycle_recur(v, graph):
    visited = {v: False for v in graph}
    path = {v: False for v in graph}

    def helper(vertex, visited, path):
        visited[vertex] = True
        path[vertex] = True
        for nbr in graph[vertex]:
            if not visited[nbr]:
                if helper(nbr, visited, path) == True:
                    return True
            elif path[nbr] == True:
                return True
        path[vertex] = False
        return False

    return helper(v, visited, path)


def detect_cycle_stack(v, graph):
    visited = {v: False for v in graph}
    stack = [v]
    path = [v]
    while stack:
        v = stack.pop()
        for nbr in graph[v]:
            if nbr in path:
                return True
            if nbr not in visited:
                visited[nbr] = True


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
