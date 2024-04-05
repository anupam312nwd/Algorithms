""" Working with Heap data structure """
import sys
import heapq

# max heap

# min heap

H = [21, 1, 45, 78, 3, 5, float('inf')]
# Covert to a heap
heapq.heapify(H)
print(H)
print('------------------------')
# Add element
heapq.heappush(H, 4)
print(H)
print('------------------------')

G = [(21, 'a'), (5, 'c'), (3, 9), (7, 't'), (4, 'b')]
print(type(G))
heapq.heapify(G)
heapq.heappop(G)
print(G)
a = heapq.nsmallest(2, G)
largestk = heapq.nlargest(3, G)
print(largestk)
print(type(largestk))
