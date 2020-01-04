'''
Dijkstra's shortest path algorithm pseudo-code:
Initialize:
    X = {s}  # [vertices processed so far]
    A[s] = 0 # [computed shortest path distances]
    # B[s] = empty path # [computed shortest paths]

Main loop:
    while X \neq V: # [need to grow X by 1 node]
        among all edges (v,w) \in E with w\in X, v\notin X,
        pick the one that minimizes A[v] + l_{vw}
        # l_{vw}
        # Dijkstra's greedy criterion
        [call it (v*, w*)]
        add w* to X
        set A[w*] := A[v*] + l_{v*w*}
        set B[w*] := B[v*] U (v*,w*)
'''
import heapq

def dijkstra(graph, vertex):
    X = {vertex}
    dist = {vertex: 0}
    V = list(graph.keys())
    H = [((float('inf'),'inf'),'inf')]

    VminusX = set(V)-set(X)
    H = []
    heap = {}
    path = {} # optional: finding shortest path
    for v in V:
        heap[v] = [(float('inf'), (v,v))]
        path[v] = [vertex]


    while X != set(V):
        for w in X:
            for v in list(set(graph[w].keys()).intersection(VminusX)):
                heapq.heappush(heap[v], (dist[w] + graph[w][v], (v,w)))

        if X == {vertex}:
            for v in VminusX:
                heapq.heappush(H, heap[v][0])

        # print(H)
        S = heapq.heappop(H)
        v = S[1][0]
        w = S[1][1]
        dist[v] = S[0]
        # print(v,w)
        # print('v: ', v, 'and w: ', w)
        X = X.union({v})
        VminusX = set(V)-set(X)
        for u in set(graph[v].keys()).intersection(VminusX):
            for j in range(len(H)):
                if H[j][1][0] == u:
                    T = H[j]
                    H.remove(T)
                    break
            if dist[v]+graph[v][u] == min(T[0], dist[v]+graph[v][u]) and T[0] != dist[v]+graph[v][u]:
                path[u].append(v) # to calculate the path
            heapq.heappush(H, (min(T[0], dist[v]+graph[v][u]), (u, T[1][1])))
            # print(H, v, u)
        # print(H)
    for v in V:
        path[v].append(v)       # adding own vertex at the end of the path

    return dist, path


graph = {
    'a': {'b':1, 'c':2, 'd':4},
    'b': {'e':4},
    'c': {'d':3},
    'd': {'e':1, 'b':2},
    'e': {}
}

# graph = {
#     'a': {'b':1, 'c':2, 'd':4},
#     'b': {'d':2},
#     'c': {'d':3},
#     'd': {},
# }

# graph = {
#     'a': [(1,'b'), (2,'c'), (4,'d')],
#     'b': [(2,'d'), (4,'e')],
#     'c': [(3,'d')],
#     'd': [(1,'e')],
#     'e': []
# }

dist, path = dijkstra(graph, 'a')
print(dist, '\n', path)

'''
Graph structure:
graph = {
    'A': [('B',2), ('C',4)],
    'B': [('C',2)],
    'C': [],
}

print(graph)
print('length of graph[\'A\']:=', len(graph['A']))
print(graph['A'][0][1])
'''
