#!/usr/bin/env python
# not working!


def paths_bet_two_points(graph, u, v):
    visited = set()
    all_paths = set()

    def _paths_bet_two_points(path, visited):
        if path[-1] == v:
            all_paths.add(tuple(path))
        else:
            for nbr in graph[path[-1]]:
                if nbr not in visited:
                    visited.add(nbr)
                    _paths_bet_two_points(path + [nbr], visited)

    _paths_bet_two_points([u], visited)
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

    paths = paths_bet_two_points(graph, "c", "b")
    print(paths)
