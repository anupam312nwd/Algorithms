'''
Quick Sort pseudo code:
    pick a random value from the array,
    Compare all other values with this and place it in right or left of this value,
    
    two function: Partition and QuickSort,
    Partition(arr A, start, end):
        # two pointers: index and i
        index = start; i = start
        n = end - start
        pivot = A[end]
        for i in range(start, end):
            if A[i] <= pivot:
                Swap(A[i], A[index])
                index += 1
        Swap(A[end], A[index])
        return index
        
    QuickSort(arr A, start, end):
        if start >= end: return
        pindex = Partition(A, start, end)
        QuickSort(A, start, pindex-1)
        QuickSort(A, pindex+1, end)
'''
import random


def Partition(A, start, end):
    index = start
    pivindex = random.randint(start, end)
    A[pivindex], A[end] = A[end], A[pivindex]
    pivot = A[end]
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[index] = A[index], A[i]
            index += 1

    A[index], A[end] = A[end], A[index]
    return index


def QuickSort(A, start, end):
    if start < end:
        pindex = Partition(A, start, end)
        QuickSort(A, start, pindex - 1)
        QuickSort(A, pindex + 1, end)


T = [14, 11, 7, 6, 2, -1, 9]
QuickSort(T, 0, len(T) - 1)
print(T)

L = 1000
a = [0] * L
for i in range(0, L):
    a[i] = random.randint(1, L)
# print(a)
QuickSort(a, 0, len(a) - 1)
print(a)
