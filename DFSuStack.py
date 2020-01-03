''' Depth First Search: Topological ordering'''
from collections import deque

def dfs(graph, start_vertex):
    val = len(graph)
    stack = deque([start_vertex])
    parent = {start_vertex: None}
    top_order = {}
    # for w in graph:
    #     top_order[w] = 0
    return dfs_visit(graph, parent, stack,  val, top_order)

def dfs_visit(graph, parent, stack,  val, top_order):

    while stack:
        v = stack[-1]
        if graph[v] != {}:
            for w in graph[v]:
                if w not in parent:
                    parent[w] = v
                    stack.append(w)
                    dfs_visit(graph, parent, stack,  val, top_order)
        if stack == deque([]): break
        #print(stack, top_order)
        u = stack.pop()
        top_order[u] = val
        val -= 1

    return parent, top_order

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': [],
    'E': ['D']
}
print(dfs(graph, 'A'))

graph2 = {
    'a':['b','c'],
    'b':['d','f','g'],
    'c':['d'],
    'd':['e'],
    'e':['g'],
    'f':['h'],
    'g':['f','h'],
    'h':[]
}

print(dfs(graph2, 'a'))



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



# # Simple:
# # a --> b
# #   --> c --> d
# #   --> d
# graph1 = {
# "a": ["b", "c", "d"],
# "b": [],
# "c": ["d"],
# "d": []
# }
# # 2 components
# graph2 = {
# "a": ["b", "c", "d"],
# "b": [],
# "c": ["d"],
# "d": [],
# "e": ["g", "f", "q"],
# "g": [],
# "f": [],
# "q": []
# }
# # cycle
# graph3 = {
# "a": ["b", "c", "d"],
# "b": [],
# "c": ["d", "e"],
# "d": [],
# "e": ["g", "f", "q"],
# "g": ["c"],
# "f": [],
# "q": []
# }

# from collections import deque
# GRAY, BLACK = 0, 1
# def topological(graph):
#     order, enter, state = deque(), set(graph), {}
# def dfs(node):
#         state[node] = GRAY
# for k in graph.get(node, ()):
#             sk = state.get(k, None)
# if sk == GRAY: raise ValueError("cycle")
# if sk == BLACK: continue
#             enter.discard(k)
#             dfs(k)
#         order.appendleft(node)
#         state[node] = BLACK
# while enter: dfs(enter.pop())
# return order
# # check how it works
# print topological(graph1)
# print topological(graph2)
# try: topological(graph3)
# except ValueError: print "Cycle!"
# # The MIT License (MIT)
# # Copyright (c) 2014 Alexey Kachayev
