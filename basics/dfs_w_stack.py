""" Depth First Search: Topological ordering"""
# from collections import deque


def dfs(graph, start_vertex):
    val = len(graph)
    stack = [start_vertex]
    parent = {start_vertex: None}
    top_order = {}
    # for w in graph:
    #     top_order[w] = 0
    return dfs_visit(graph, parent, stack, val, top_order)


def dfs_visit(graph, parent, stack, val, top_order):

    while stack:
        v = stack[-1]
        for w in graph[v]:
            if w not in parent:
                parent[w] = v
                stack.append(w)
                dfs_visit(graph, parent, stack, val, top_order)
        if stack == []:
            break
        # print(stack, top_order)
        u = stack.pop()
        top_order[u] = val
        val -= 1

    return parent, top_order


graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["D"], "D": [], "E": ["D"]}
print(dfs(graph, "A"))

graph2 = {
    "a": ["b", "c"],
    "b": ["d", "f", "g"],
    "c": ["d"],
    "d": ["e"],
    "e": ["g"],
    "f": ["h"],
    "g": ["f", "h"],
    "h": [],
}

print(dfs(graph2, "a"))


# def dfs(graph, start_vertex):
#     val = len(graph)
#     stack = deque([start_vertex])
#     parent = {start_vertex: None}
#     # top_order = {start_vertex: 1}
#     top_order = {}
#     for w in graph:
#         top_order[w] = 0
#     return dfs_visit(graph, parent, stack, start_vertex, val, top_order)

# def dfs_visit(graph, parent, stack, v, val, top_order)
#     while stack:
#         for w in graph[v]:
#             if w not in parent:
#                 parent[w] = v
#                 stack.append(w)
#                 dfs_visit(graph, parent, stack, w, val, top_order)
#             u = stack.pop()
#             top_order[u] = val
#             val -= 1
#     return parent, top_order
