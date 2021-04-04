#!/usr/bin/env python

import sys
import numpy as np

# f = open("case_sample.txt", "r")
f = open("case3.txt", "r")
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
print(N)
print("--------------------------------------------------")

col_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)
count = 0


indr = np.argmin(row_sum)
indc = np.argmin(col_sum)
N = len(row_sum)

axs, min_val = (
    (1, row_sum[indr]) if row_sum[indr] <= col_sum[indc] else (0, col_sum[indc])
)

if min_val == 0:
    arr = np.delete(arr, indc, 1)
    arr = np.delete(arr, indr, 0)

print(arr)
