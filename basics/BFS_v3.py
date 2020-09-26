#!/usr/bin/env python

"""bfs traversal: using queue
   does not support multiple paths
   give shortest path length
"""

from collections import deque

def bfs_traversal(graph, node):
    visited = {node}
    que = deque(node)
    traverse = []
    path = {}

    while que:
        t = que.popleft()
        traverse.append(t)
        if t not in path:
            path[t] = [t]
        for k in graph[t]:
            if k not in visited:
                path[k] = path[t] + [k]
                que.append(k)
                visited.add(k)

    return traverse, path


def short_path_len(graph, paths):
    short_path_len = {}
    for v in graph:
        short_path_len[v] = len(paths[v]) - 1
    return short_path_len

def parents(graph, paths):
    parents = {}
    for v in graph:
        if len(paths[v]) >= 2:
            parents[v] = paths[v][-2]
        else:
            parents[v] = None
    return parents


graph = {
    'a': ['b', 'd', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'i'],
    'd': ['a', 'b', 'h'],
    'e': ['b', 'f'],
    'f': ['e'],
    'h': ['d', 'i'],
    'i': ['h', 'k'],
    'k': ['i']
}

traverse, paths = bfs_traversal(graph, 'a')
print(traverse)
print(paths)
print(short_path_len(graph, paths))
print(parents(graph, paths))
