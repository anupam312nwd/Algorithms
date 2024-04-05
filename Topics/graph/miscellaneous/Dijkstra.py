"""
Dijkstra's shortest path algorithm pseudo-code:
Initialize:
    previous [node] = node
    distances [vertices] = float('inf')

dijkstra(graph, vertex):
    maintain min-heap for
"""

import heapq


def find_shortest_path(previous):
    shortest_paths = {node: [] for node in previous.keys()}
    for node in previous.keys():
        current = node
        while previous[current] is not None:
            shortest_paths[node].append(previous[current])
            current = previous[current]
        shortest_paths[node].reverse()
        shortest_paths[node].append(node)
    return shortest_paths


def dijkstra(graph, node):
    distances = {vertex: float('inf') for vertex in graph.keys()}
    heap = [(distances[vertex], vertex) for vertex in graph.keys()]
    heapq.heapify(heap)

    previous = {node: None}
    distances[node] = 0
    heapq.heappush(heap, (distances[node], node))

    while heap:
        current_distance, vertex = heapq.heappop(heap)
        if current_distance > distances[vertex]:
            continue
        for neighbour, weight in graph[vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                heapq.heappush(heap, (distance, neighbour))
                distances[neighbour] = distance
                previous[neighbour] = vertex
    return distances, previous


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

    # dist, parent = dijkstra(graph, "a")
    distances, previous = dijkstra(graph, "a")
    print(distances)
    print(previous)
    print('--------------------------')
    shortest_paths = find_shortest_path(previous)
    print(shortest_paths)

    """
    Output:
    {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
     {'a': ['a', 'a'], 'b': ['a', 'b'], 'c': ['a', 'c'], 'd': ['a', 'b', 'd'],\
    'e': ['a', 'b', 'd', 'e']}
    just added a line here: test.
    """
