#!/usr/bin/env python

import sys
import numpy as np

# arr = np.random.randint(0, 1, (7, 7))

f = open("case_sample.txt", "r")
data = f.read()

# data = sys.stdin.read()

for num, line in enumerate(data.split("\n")):
    if line:
        if num == 0:
            N = int(line)
            arr = np.empty([N, N], dtype=int)
        else:
            lst = line.split(",")
            lst_int = [int(x) for x in lst]
            arr[num - 1] = lst_int
            # mat_lst.append(lst_int)

print(arr)
print("--------------------------------------------------")
print(arr[0, :])
print(arr[:, 0])

print(float("inf"))

a, b = 2, (3, 4)
print(a)
print(b)
