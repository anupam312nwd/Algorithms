#!/usr/bin/env python

def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for nbr in graph[vertex]:
            dfs(graph, nbr, visited)



graph = {
    'a': ['b', 'd', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'i'],
    'd': ['a', 'b', 'h'],
    'e': ['b', 'f'],
    'f': ['e'],
    'h': ['d', 'i'],
    'i': ['h', 'k', 'c'],
    'k': ['i']
}

print(dfs(graph, 'a'))

vertex = 'a'
visited = {'d'}
print(list(set(graph[vertex])-visited))
print(graph[vertex])
# for nbr in graph[vertex]:
#     print(vertex, nbr)
