graph = {
    'A': [('B',2), ('C',4)],
    'B': [('C',2)],
    'C': [],
}

print(graph)
print('length of graph[\'A\']:=', len(graph['A']))
print(graph['A'][0][1])
print(type(graph['A']))

print('---------------')
a = [('b',2),('c',3)]
print(type(a))
print(a[0][1])
