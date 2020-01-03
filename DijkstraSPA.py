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
    A = {vertex: 0}
    V = list(graph.keys())
    H = [((float('inf'),'inf'),'inf')]

    VminusX = set(V)-set(X)
    H = []
    heap = {}
    for v in V:
        heap[v] = [(float('inf'), (v,v))]

    ## for all edges (v,w) with w \in X, v \in VminusX
    # X = X.union({'b'})
    # VminusX = set(V)-set(X)
    # for w in X:
    #     for v in list(set(graph[w].keys()).intersection(VminusX)):
    #         heap[v].append((graph[w][v], (v,w)))
    #         print('heap['+v+']:', heap[v])
    #     # heapq.heapify(heap[v])
    # print('--------------------------------')
    # for v in VminusX:
    #     heapq.heapify(heap[v])
    #     print('heap['+v+']:', heap[v])
    #     H.append(heap[v][0])
    # heapq.heapify(H)
    # print(H) # [(2, ('c', 'a')), (4, ('e', 'b')), (2, ('d', 'b'))]

    while X != V:
        VminusX = set(V)-set(X)
        for w in X:
            for v in list(set(graph[w].keys()).intersection(VminusX)):
                heap[v].append((graph[w][v], (v,w)))
                print('heap['+v+']:', heap[v])
        print('--------------------------------')
        for v in VminusX:
            heapq.heapify(heap[v])
            print('heap['+v+']:', heap[v])
            H.append(heap[v][0])
        heapq.heapify(H)
        print(H)

        S = heapq.heappop(H)
        v = S[1][0]
        w = S[1][1]


graph = {
    'a': {'b':1, 'c':2, 'd':4},
    'b': {'d':2, 'e':4},
    'c': {'d':3},
    'd': {'e':1},
    'e': {}
}


# graph = {
#     'a': [(1,'b'), (2,'c'), (4,'d')],
#     'b': [(2,'d'), (4,'e')],
#     'c': [(3,'d')],
#     'd': [(1,'e')],
#     'e': []
# }

dijkstra(graph, 'a')

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
