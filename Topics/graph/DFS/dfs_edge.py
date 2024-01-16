#!/usr/bin/env python


def dfs_by_edge(graph, vertex):
    marked = []
    dfs_tree = []
    marked.append(vertex)
    _dfs_by_edge(graph, vertex, marked, dfs_tree)
    return marked, dfs_tree


def _dfs_by_edge(graph, vertex, marked, dfs_tree):
    for nbr in graph[vertex]:
        if nbr not in marked:
            marked.append(nbr)
            dfs_tree.append((vertex, nbr))
            _dfs_by_edge(graph, nbr, marked, dfs_tree)


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["D"], "D": ["F"], "E": ["D"], "F": []}

print(dfs_by_edge(graph, "A"))
