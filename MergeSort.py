"""
Pseudo codes for Merge Sort (Divide and Conquer paradigm):
Two operations: Merge, and Sort:
Pseudo code:
    def Merge(Array A, Array B):
        n = sum of array length A and B
        initialze array C of size n
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        elif A[i] > B[j]:
            C[k] = B[j]
            j += 1

    def Sort(Array T):
        n = len(T)
        if n == 1: return T # base case
        split T into two halves
        F = Sort(first half)
        G = Sort(second half)
        Merge(F, G)


Between pseudo code and actual code:
    def Merge(array A, array B):
        n = A.length + B.length
        C = [0]*n
        i,j = 0,0
        for k in range(0, n-1):
            if i == A.length:
                C(k) = B(j)
                j++
            elif j == B.length:
                C(k) = A(i)
                i++
            elif A(i) < B(j):
                C(k) = A(i)
                i++
            elif A(i) > B(j):
                C(k) = B(j)
                j++
        return C

    def Sort(array T):
        m = len(T)
        Merge(Sort(T[0:floor(m/2)]), Sort(T[floor(m/2)+1:m]))
"""

import math

def Merge(A, B):  # Merge is working fine
    l = len(A)
    m = len(B)
    n = l+m
    C = [0]*n
    i,j = 0,0
    for k in range(0, n):
        if i < l and j < m:
            if A[i] <= B[j]:
                C[k] = A[i]
                i += 1
            else:
                C[k] = B[j]
                j += 1
        elif i < l:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
    return C

def Sort(T):
    m = len(T)
    if m == 1: return T # Base case
    t = math.floor(m/2)
    F = Sort(T[0:t])
    G = Sort(T[t:m])
    return Merge(F, G)

T = [14, 11, 7, 6, 20, 8, -1, 0, 3, 11]
print(Sort(T))


import random
L = 1000000
a = [0]*L
for i in range(0, L):
    a[i] = random.randint(1, L)
b = Sort(a)
#print(a)
#print(b)
