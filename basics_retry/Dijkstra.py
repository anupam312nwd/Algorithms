"""
Dijkstra's shortest path algorithm pseudo-code:
Initialize:
    parent [vertices] = -1
    distances [vertices] = float('inf')

dijkstra(graph, vertex):
    maintain min-heap for
"""

import heapq


def dijkstra(graph, vertex0):
    all_vertices = graph.keys()
    visited = set()
    parent = {}
    distances = {}
    heap = []
    not_visited = {vertex0}
    for ver in all_vertices:
        distances[ver] = float("inf")
        if ver != vertex0:
            not_visited.add(ver)
            parent[ver] = -1
            heapq.heappush(heap, (float("inf"), ver))
        else:
            parent[vertex0] = -1
            heapq.heappush(heap, (0, vertex0))

    while not_visited and heap:
        val, ver = heapq.heappop(heap)
        if distances[ver] > val:
            distances[ver] = val
            visited.add(ver)
        if ver in not_visited:
            not_visited.remove(ver)

        for nbr in graph[ver]:
            temp_dist = distances[ver] + graph[ver][nbr]
            if nbr in not_visited and distances[nbr] > temp_dist:
                distances[nbr] = temp_dist
                parent[nbr] = ver
                heapq.heappush(heap, (temp_dist, nbr))

    return distances, parent


if __name__ == "__main__":

    graph = {
        "a": {"b": 1, "c": 2, "d": 4},
        "b": {"d": 2, "e": 4},
        "c": {"d": 3},
        "d": {"e": 1},
        "e": {},
        "f": {"g": 2},
        "g": {"h": 1},
        "h": {},
    }

    dist, parent = dijkstra(graph, "a")
    print(dist, parent)

    """
    Output:
    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
     {'a': ['a', 'a'], 'b': ['a', 'b'], 'c': ['a', 'c'], 'd': ['a', 'b', 'd'],\
    'e': ['a', 'b', 'd', 'e']}
    just added a line here: test.
    """
