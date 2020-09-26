""" Route between nodes:
    given a directed graph, design an algorithm to find out whether there is a route between two nodes.
    use bfs to traverse through all nodes, starting from a node, then check whether the other node is
    in the traveresed nodes.
"""

from collections import deque


def bfs_traverse(graph, node):

    traverse = {node}
    paths = {node: [node]}
    que = deque(node)

    while que:
        t = que.popleft()
        for v in graph[t]:
            if v not in traverse:
                traverse.add(v)
                que.append(v)
                paths[v] = paths[t] + [v]
    return traverse, paths


def short_path_len(graph, paths):
    short_path_len = {}
    for v in graph:
        short_path_len[v] = len(paths[v]) - 1
    return short_path_len

def parents(graph, paths):
    parents = {}
    for v in graph:
        if len(paths[v]) >= 2:
            parents[v] = paths[v][-2]
        else:
            parents[v] = None
    return parents

graph = {
    'a': ['b', 'd', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'i'],
    'd': ['a', 'b', 'h'],
    'e': ['b', 'f'],
    'f': ['e'],
    'h': ['d', 'i'],
    'i': ['h', 'k'],
    'k': ['i'],
    's': ['t']
}

traverse, paths = bfs_traverse(graph, 'a')
print(traverse)
print(paths)

# print(short_path_len(graph, paths))
# print(parents(graph, paths))

def route_bet_nodes(graph, node1, node2):
    traverse, paths = bfs_traverse(graph, node1)
    if node2 in traverse:
        return True
    else:
        return False

print("connectecd route" if route_bet_nodes(graph, 'a', 'c') else "not connected route")
print("connectecd route" if route_bet_nodes(graph, 'a', 's') else "not connected route")
