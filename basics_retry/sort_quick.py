#!/usr/bin/env python


def Partition(A, start, end):
    index = start
    pivot = A[end]
    for i in range(start, end+1):
        if A[i] <= pivot:
            A[i], A[index] = A[index], A[i]
            index += 1

    # A[index], A[end] = A[end], A[index]
    return (index-1)

def QuickSort(A, start, end):
    if start < end:
        pindex = Partition(A, start, end)
        QuickSort(A, start, pindex-1)
        QuickSort(A, pindex+1, end)

T = [14, 11, 7, 6]
QuickSort(T, 0, len(T)-1)
print(T)

import random
L = 100
a = [0]*L
for i in range(0, L):
    a[i] = random.randint(1, L)
#print(a)
QuickSort(a, 0, len(a)-1)
print(a)
