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


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["D"], "D": [], "E": ["D"]}

    print(dfs(graph, "A"))
