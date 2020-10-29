import heapq
import scipy

print(scipy.__version__)
heap = [(float("inf"), "a")]
heapq.heappush(heap, (7, "b"))
heapq.heappush(heap, (5, "c"))
heapq.heappush(heap, (8, "d"))
heapq.heappush(heap, (3, "e"))

print(heap)

hp = []
# a = heapq.heappop(heap)
i, j = heapq.heappop(heap)
print("--------------------------------------------------")
print(i, j)

hp.append(heapq.heappop(heap))
print("--------------------------------------------------")
print(hp)
print(heap)
print("--------------------------------------------------")
print(type(heap))


lsta = [(1, "e"), (4, "b"), (2, "a"), (7, "d")]
lstb = [(1, "e"), (4, "b"), (2, "a"), (5, "d")]

heapq.heapify(lsta)
heapq._heapify_max(lstb)

print("--------------------------------------------------")
print(lsta)
print(lstb)
