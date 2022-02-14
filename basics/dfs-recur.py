#!/usr/bin/env python


def dfs_recur(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for nbr in graph[vertex]:
            dfs_recur(graph, nbr, visited)


if __name__ == "__main__":
    graph = {
        "a": ["b", "d", "c"],
        "b": ["a", "d", "e"],
        "c": ["a", "i"],
        "d": ["a", "b", "h"],
        "e": ["b", "f"],
        "f": ["e"],
        "h": ["d", "i"],
        "i": ["h", "k", "c"],
        "k": ["i"],
    }
    dfs_recur(graph, "a")
