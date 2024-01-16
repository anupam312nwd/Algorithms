#!/usr/bin/env python

from draw_graph.graph_from_dict import plot_graph_from_dict


def get_paths_bet_two_points(graph, u, v, visited=None, all_paths=None):
    if visited is None:
        visited = set()
    if all_paths is None:
        all_paths = set()
    stack = [(u)]
    while stack:
        path = list(stack.pop())
        w = path[-1]
        if w == v:
            all_paths.add(tuple(path))
        else:
            if w not in visited:
                visited.add(w)
                for nbr in graph[w]:
                    if nbr not in visited:
                        stack.append(tuple(list(path) + [nbr]))
    return all_paths


if __name__ == "__main__":
    graph = {
        "a": ["b", "d", "c"],
        "b": ["a", "d", "e"],
        "c": ["a", "g"],
        "d": ["a", "b", "f"],
        "e": ["b"],
        "f": ["d", "g"],
        "g": ["f", "c"],
    }

    plot_graph_from_dict(graph, direction=True)
    paths = get_paths_bet_two_points(graph, "c", "b")
    print(paths)
