#!/usr/bin/env python


def allPathsBetweenSourceTarget(graph, source, target):
    paths = []
    visited = set()

    def dfs(node, target, path):
        visited.add(node)
        path.append(node)
        if node == target:
            paths.append(path[:])
        else:
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr, target, path)

        visited.remove(node)
        path.pop()
