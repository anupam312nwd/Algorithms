#!/usr/bin/env python3;  # -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:23:47 2020;    @author: anupam
Pseudo-code for BFS (Graph G, start vertex s)
mark s explored
let Q queue dataset (FIFO) initialized w s
while Q \neq empty:
    remove the first node of Q, call it v
    for each edge (v,w):
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
"""

from collections import deque


def BFS(graph, vertex):
    Queue = deque([vertex])
#    level = {vertex:0}
    parent = {vertex: None}
#    i = 1
    path = {}
    for v in graph:
        path[v] = [v]

    while Queue:
        v = Queue.popleft()     # if use _.pop(), then act as stack
        for w in graph[v]:
            if w not in parent:   # if w not in level
                # level[w] = i
                parent[w] = v
                path[w] = path[v] + path[w]
                Queue.append(w)
#        i += 1
    level = {}
    for v in graph:
        level[v] = len(path[v]) - 1
    return level, parent, path


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

# level, parent, path = BFS(graph, 'A')
# print(level, '\n', parent, '\n', path)
# print('-----------------------------------------------')
# print(BFS(graph, 'C'))
# print('-----------------------------------------------')
# print(BFS(graph, 'D'))

graph2 = {
    # 's' : ['a', 'b'],
    # 'a' : ['s', 'c'],
    # 'b' : ['s', 'c', 'd'],
    # 'c' : ['a', 'b', 'd', 'e'],
    # 'd' : ['b', 'c', 'e'],
    # 'e' : ['c', 'd'],
    'f': ['g', 'h'],
    'g': ['f', 'i', 'j'],
    'h': ['f', 'i'],
    'i': ['g', 'h', 'j'],
    'j': ['g', 'i']

}

level, parent, path = BFS(graph2, 'f')
print(level, '\n', path)
