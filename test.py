import heapq
graph = {
    'a': [(1,'b'), (2,'c'), (4,'d')],
    'b': [(2,'d'), (4,'e')],
    'c': [(3,'d')],
    'd': [(1,'e')],
    'e': []
}

print(graph['a'])
print(type(graph['a']))
print('------------------------')

graph = {
    'a': {'b':1, 'c':2, 'd':4},
    'b': {'d':2, 'e':4},
    'c': {'d':3},
    'd': {'e':1},
    'e': {}
}
print(graph['a'], type(graph['a']))
print(graph['a']['d'], list(graph.keys()), list(graph['a'].keys()))
print('------------------------')

data = [(4, {'b':'a'}), (2, {'c':'a'})]
# data = {4: {'b':'a'}, 2: {'c':'a'}}
# data = [(4, ('b','a')), (2, ('c','a'))]
# data = [(4, 'a'), (2, 'a')]
heapq.heapify(data)
print('data: ', data)
T_n = heapq.heappop(data)
print(T_n, data)
# print(heapq.heapify(list(graph['a'])))
print('------------------------')
# print(set(graph.keys()))
# print(set(graph['a'].keys()))

# S = (2, ('c', 'a'))
# print(type(S), S[1][1])
# # u = 
# V = list(graph.keys())
# print(V)

H = [(1, ('d', 'b')), (4, ('e', 'b')), (2, ('c', 'a'))]
print(H[1], type(H))
# H.remove(H[1])
for j in range(len(H)):
    if H[j][1][0] == 'e':
        T = H[j]
        H.remove(H[j])
        break
    print(j)
print(H)
print(T, T[0])
