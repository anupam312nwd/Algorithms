#!/usr/bin/env python
""" return prime factorization
"""


import math


def return_prime_factorization(N):
    """ return list of prime factorization of int n
    """
    lst = []
    while N % 2 == 0:
        lst.append(2)
        N = N/2

    while N > 0:
        val = True
        for i in range(3, int(math.sqrt(N))+1, 2):
            if N % i == 0:
                lst.append(i)
                N = N/i
                val = False
        if val == True:
            break
    if N>1:
        lst.append(int(N))

    return sorted(lst)


if __name__ == '__main__':
    N = 360
    print(return_prime_factorization(N))
