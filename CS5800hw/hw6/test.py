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

col_sum = np.sum(arr, axis=0)
row_sum = np.sum(arr, axis=1)

print(row_sum)
print(col_sum)
print("--------------------------------------------------")

indr = np.argmin(row_sum)
indc = np.argmin(col_sum)
N = len(row_sum)

# print(row_sum[indr])

# axs, min_val = (indr, row_sum[indr]) if row_sum[indr] <= col_sum[indc] else (indc, col_sum[indc])
axs, min_val = (
    (1, row_sum[indr]) if row_sum[indr] <= col_sum[indc] else (0, col_sum[indc])
)
min_sum = float("inf")

if axs == 1:
    w = np.where(row_sum == min_val)[0]
    print("r : ", w, [row_sum[x] for x in w])
    print("row_sum: ", row_sum[w])
    print("col_sum: ", col_sum[w])

    for i in w:
        temp_arr = arr[i, :]
        for j in range(N):
            if temp_arr[j] == 1:
                if min_sum > col_sum[j]:
                    min_sum, final_index = col_sum[j], (i, j)

else:
    w = np.where(col_sum == min_val)[0]
    print("c : ", w, [col_sum[x] for x in w])

    for i in w:
        temp_arr = arr[:, i]
        for j in range(N):
            if temp_arr[j] == 1:
                if min_sum > row_sum[j]:
                    min_sum, final_index = row_sum[j], (j, i)


print(axs, min_val)
print("--------------------------------------------------")
arr = np.delete(arr, i, 0)
arr = np.delete(arr, j, 1)

# print(indr)
# print(indc)
print(arr)
