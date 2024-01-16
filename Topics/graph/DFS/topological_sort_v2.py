#!/usr/bin/env python
# return topological_sort if exists
# return False if contains a cycle

from collections import defaultdict
from collections import deque


def _dfs(node, visiting, visited, graph, top_order):
    visited[node] = True
    visiting.add(node)
    for v in graph[node]:
        if v in visiting:
            return False
        if visited[v] is False:
            val = _dfs(v, visiting, visited, graph, top_order)
            if val is False:
                return False
    top_order.appendleft(node)
    visiting.remove(node)
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


if __name__ == "__main__":

    graph = defaultdict(lambda: [])
    graph["c"] = ["a", "b"]
    graph["a"] = ["d"]
    graph["b"] = ["d"]
    graph["d"] = ["g"]
    graph["e"] = ["a", "d", "f"]
    graph["g"] = ["h"]
    graph["f"] = ["h", "i"]
    # graph["f"] = ["h"]
    # graph["i"] = ["f"]
    graph["h"] = ["i"]
    graph["k"] = ["l"]
    graph["j"] = ["l", "k"]

    # graph["a"] = ["b"]
    # graph["b"] = ["c"]
    # # graph["c"] = ["a"]
    # graph["a"] = ["c"]

    top_sort_ord = top_sort(graph)
    print(top_sort_ord)
