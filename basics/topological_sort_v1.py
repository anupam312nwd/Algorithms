#!/usr/bin/env python
# contains error, not detecting cycle in graph

from collections import defaultdict
from collections import deque

graph = defaultdict(lambda: [])
graph["c"] = ["a", "b"]
graph["a"] = ["d"]
graph["b"] = ["d"]
graph["d"] = ["g"]
graph["e"] = ["a", "d", "f"]
graph["g"] = ["h"]
graph["f"] = ["h"]


def _dfs(node, visited, graph, top_order):
    visited[node] = True
    for v in graph[node]:
        if visited[v] is False:
            _dfs(v, visited, graph, top_order)
    top_order.appendleft(node)


def top_sort(graph):

    visited = dict()
    for v in graph:
        if v not in visited:
            visited[v] = False
        for w in graph[v]:
            if w not in visited:
                visited[w] = False

    n = len(visited)
    top_order = deque([])

    for node in visited:
        if visited[node] is False:
            _dfs(node, visited, graph, top_order)

    return top_order


top_sort_ord = top_sort(graph)
print(top_sort_ord)
