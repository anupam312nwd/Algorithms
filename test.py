graph = {
    'a': [(1,'b'), (2,'c'), (4,'d')],
    'b': [(2,'d'), (4,'e')],
    'c': [(3,'d')],
    'd': [(1,'e')],
    'e': []
}

print(graph['a'])
print(type(graph['a']))

graph = {
    'a': [{'b':1}, {'c':2}, {'d':4}],
    'b': [{'d':2}, {'e':4}],
    'c': [{'d':3}],
    'd': [{'e':1}],
    'e': []
}
print(graph['a'])
print(type(graph['a']))

