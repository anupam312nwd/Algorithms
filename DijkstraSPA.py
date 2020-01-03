'''
Dijkstra's shortest path algorithm pseudo-code:
Initialize:
    X = {s}  # [vertices processed so far]
    A[s] = 0 # [computed shortest path distances]
    # B[s] = empty path # [computed shortest paths]

Main loop:
    while X \neq V: # [need to grow X by 1 node]
        among all edges (v,w) \in E w v\in X, w\notin X,
        pick the one that minimizes A[v] + l_{vw}
        # Dijkstra's greedy criterion
        [call it (v*, w*)]
        add w* to X
        set A[w*] := A[v*] + l_{v*w*}
        set B[w*] := B[v*] U (v*,w*)
'''





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
