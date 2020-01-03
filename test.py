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
data = {4: {'b':'a'}, 2: {'c':'a'}}
# data = [(4, ('b','a')), (2, ('c','a'))]
# data = [(4, 'a'), (2, 'a')]
print(data)
heapq.heapify(list(data))
print(data)
# print(heapq.heapify(list(graph['a'])))
print('------------------------')
print(set(graph.keys()))
print(set(graph['a'].keys()))

