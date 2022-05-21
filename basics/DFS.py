"""Depth First Search: recursive (without using Stack)."""


def dfs(graph, vertex):
    """Return parents using graph and vertex."""
    parents = {vertex: None}
    dfs_visit(graph, vertex, parents)
    return parents


def dfs_visit(graph, vertex, parents):
    """Traverse recursively."""
    for w in graph[vertex]:
        if w not in parents:
            parents[w] = vertex
            dfs_visit(graph, w, parents)


def dfs_recur(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for nbr in graph[vertex]:
            dfs_recur(graph, nbr, visited)


def dfs_stack(graph, ver):
    visited = {ver}
    stack = [ver]

    while stack:
        ver = stack.pop()
        print(ver)
        for nbr in graph[ver]:
            if nbr not in visited:
                stack.append(nbr)
                visited.add(nbr)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["D"], "D": [], "E": ["D"]}

    print(dfs(graph, "A"))

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
    # dfs_stack(graph, "a")
