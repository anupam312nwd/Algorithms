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
    graph = {
        "a": ["b", "c"],
        "b": ["d", "f", "g"],
        "c": ["d"],
        "d": ["e"],
        "e": ["g"],
        "f": ["h"],
        "g": ["f", "h"],
        "h": [],
    }
    dfs_stack(graph, "a")
