#!/usr/bin/env python

def recursive_multiply(a, b):
    if (a==0) or (b==0):
        return 0
    if (a==1) and (b==1):
        return 1
    m1 = int(a/2)
    m2 = a-m1
    n1 = int(b/2)
    n2 = b-n1
    return recursive_multiply(m1, n1) + recursive_multiply(m1, n2) + recursive_multiply(m2, n1) + recursive_multiply(m2, n2)

j = 657
k = 722
print(recursive_multiply(j, k)==j*k)
