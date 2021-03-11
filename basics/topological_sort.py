#!/usr/bin/env python
# contains error, not detecting cycle in graph

from collections import defaultdict
from collections import deque

graph = defaultdict(lambda: [])
# graph["c"] = ["a", "b"]
# graph["a"] = ["d"]
# graph["b"] = ["d"]
# graph["d"] = ["g"]
# graph["e"] = ["a", "d", "f"]
# graph["g"] = ["h"]
# graph["f"] = ["h", "i"]
# graph["h"] = ["i"]
# graph["k"] = ["l"]
# graph["j"] = ["l", "k"]

graph["a"] = ["b"]
graph["b"] = ["c"]
graph["c"] = ["a"]
# graph["a"] = ["c"]


def _dfs(node, visiting, visited, graph, top_order):
    visited[node] = True
    visiting.add(node)
    for v in graph[node]:
        if visited[v] is False:
            if v in visiting:
                return False
            val = _dfs(v, visiting, visited, graph, top_order)
            if val is False:
                return False
    top_order.appendleft(node)
    return True


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
            visiting = set()
            boolval = _dfs(node, visiting, visited, graph, top_order)
            if boolval is False:
                return False

    return top_order


top_sort_ord = top_sort(graph)
print(top_sort_ord)
