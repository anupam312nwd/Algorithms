""" Working with Heap data structure """
import sys
import heapq

# max heap

# min heap

H = [21, 1, 45, 78, 3, 5, float('inf')]
# Covert to a heap
heapq.heapify(H)

print(H)
print(heapq.heappop(H))
