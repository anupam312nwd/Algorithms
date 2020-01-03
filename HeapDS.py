''' Working with Heap data structure '''
import heapq
H = [21,1,45,78,3,5, float('inf')]
# Covert to a heap
heapq.heapify(H)
print(H)
print('------------------------')
# Add element
heapq.heappush(H,4)
print(H)
print('------------------------')
# Remove element from the heap
heapq.heappop(H)
print(H)
print('------------------------')

G = {21: 'a',1:'b',45:'c',78:'d',3:'e',5:'f', float('inf'):'g'}
print(type(G))
# heapq.heapify(G)
# print(G)
print('------------------------')
F = [(21, 'a'), (4, 'b')]
print(type(F))
heapq.heapify(F)
print(F)
print('------------------------')
graph = {
    'a': [(1,'b'), (2,'c'), (4,'d')],
    'b': [(2,'d'), (4,'e')],
    'c': [(3,'d')],
    'd': [(1,'e')],
    'e': []
}

print('------------------------')
heapq.heapify(graph['a'])
print(graph['a'])
for v in graph:
    heapq.heapify(graph[v])
    print('-->', graph[v])
print('------------------------')
heap = {}
# H = [(float('inf'))]
H = [((float('inf'),'inf'),'inf')]
for v in graph:
    if graph[v] != []:
        heap[v] = [(heapq.heappop(graph[v]),v)]
        print(type(heap[v]),heap[v])
        H = H + heap[v]

print(heap['a']+heap['b'])
print('------------------------')
print(H)
heapq.heapify(H)
print('------------------------')
print(H)
print(H[0][0][0], H[0][0][1], H[0][1])

# print(graph['a'])
# print(heap['a'])
# print(graph['a'][0][0],graph['a'][0][1])
