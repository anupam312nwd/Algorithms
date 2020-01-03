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
    for i in range(len(graph[vertex])):
        A[graph[vertex][i][1]] = graph[vertex][i][0]
    print(A)

    VminusX = list(set(V)-set(X))
    H = []
    heap = {}
    # for v in VminusX:
    #     if graph[v] != []:
    #         heapq.heapify(graph[v])
    #         heap[v] = [(heapq.heappop(graph[v]),v)]
    #         H = H + heap[v]
    #     else:
    #         heap[v] = [((float('inf'),'inf'),v)]
    #         H = H + heap[v]
    # heapq.heapify(H)
    # print(H)

    for v in VminusX: # 
        for w in X:
            heap[v] = 

    # while X != V:
    #     VminusX = list(set(V)-set(X))
        



graph = {
    'a': [(1,'b'), (2,'c'), (4,'d')],
    'b': [(2,'d'), (4,'e')],
    'c': [(3,'d')],
    'd': [(1,'e')],
    'e': []
}

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
