''' Depth First Search: (without using Stack)'''


def dfs(graph, vertex):
    parents = {vertex: None}
    dfs_visit(graph, vertex, parents)
    return parents


def dfs_visit(graph, vertex, parents):
    for w in graph[vertex]:
        if w not in parents:
            parents[w] = vertex
            dfs_visit(graph, w, parents)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': [],
    'E': ['D']
}
print(dfs(graph, 'A'))

# def dfs(graph, vertex):
#     parents = {vertex: None}
#     f = {}
#     dfs_visit(graph, vertex, parents, f)
#     return parents, f

# def dfs_visit(graph, vertex, parents, f):
#     num_vertices = len(graph)
#     current_label = num_vertices
#     for w in graph[vertex]:
#         if w not in parents:
#             parents[w] = vertex
#             dfs_visit(graph, w, parents, f)
#     f[w] = current_label
#     current_label -= 1

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C', 'E'],
#     'E': ['B', 'D']
# }

# print(dfs(graph, 'A'))
