#!/usr/bin/env python


import sys
import numpy as np

f = open("case_sample.txt", "r")
# f = open("case2.txt", "r")
data = f.read()

# data = sys.stdin.read()

arr = []
for num, line in enumerate(data.split("\n")):
    if line:
        if num == 0:
            N = int(line)
            # arr = np.empty([N, N], dtype=int)
        else:
            lst = line.split(",")
            lst_int = [int(x) for x in lst]
            # arr[num - 1] = lst_int
            arr.append(lst_int)

print(arr)
print(N)
print("--------------------------------------------------")

print(arr[0])
print(len(arr[0]))
# col_sum = np.sum(arr, axis=0)


def arr_col_sum(arr):
    col_sum_mat = []
    N = len(arr[0])
    for i in range(N):
        col_s = 0
        for j in range(N):
            col_s += arr[j][i]
        col_sum_mat.append(col_s)
    return col_sum_mat


def arr_row_sum(arr):
    row_sum_mat = []
    N = len(arr[0])
    for i in range(N):
        row_s = 0
        for j in range(N):
            row_s += arr[i][j]
        row_sum_mat.append(row_s)
    return row_sum_mat


def arr_col_del(arr, col_ind):
    for row in arr:
        del row[col_ind]
    # return arr


def arr_row_del(arr, row_ind):
    del arr[row_ind]
    # return arr


def arr_arg_min(arr):
    ar_min = float("inf")
    arg = 0
    for i, val in enumerate(arr):
        if val < ar_min:
            arg, ar_min = i, val
    return arg, ar_min


def arr_get_col(arr, col_ind):
    N = len(arr[0])
    arr_col = [arr[i][col_ind] for i in range(N)]
    return arr_col


def arr_get_row(arr, row_ind):
    return arr[row_ind]


print("arr_get_col: ", arr_get_col(arr, 1))
print("arr_get_row: ", arr_get_row(arr, 1))
print("--------------------------------------------------")
col_sum = arr_col_sum(arr)
row_sum = arr_row_sum(arr)

print(col_sum)
print(row_sum)

print("--------------------------------------------------")
arr_col_del(arr, 1)
for row in arr:
    print(row)

print("--------------------------------------------------")
arr_row_del(arr, 1)
for row in arr:
    print(row)

indr, row_min = arr_arg_min(row_sum)
# row_sum = np.sum(arr, axis=1)
# count = 0

# while arr.any() or np.sum(row_sum) != 0:

#     indr = np.argmin(row_sum)
#     indc = np.argmin(col_sum)
#     N = len(row_sum)

#     axs, min_val = (
#         (1, row_sum[indr]) if row_sum[indr] <= col_sum[indc] else (0, col_sum[indc])
#     )

#     if min_val == 0:
#         arr = np.delete(arr, indc, 1)
#         arr = np.delete(arr, indr, 0)

#     else:
#         min_sum = float("inf")

#         if axs == 1:
#             w = np.where(row_sum == min_val)[0]

#             for i in w:
#                 temp_arr = arr[i, :]
#                 for j in range(N):
#                     if temp_arr[j] == 1:
#                         if min_sum > col_sum[j]:
#                             min_sum, final_index = col_sum[j], (i, j)

#         else:
#             w = np.where(col_sum == min_val)[0]
#             print("c : ", w, [col_sum[x] for x in w])

#             for i in w:
#                 temp_arr = arr[:, i]
#                 for j in range(N):
#                     if temp_arr[j] == 1:
#                         if min_sum > row_sum[j]:
#                             min_sum, final_index = row_sum[j], (j, i)

#         count += 1

#         arr = np.delete(arr, i, 0)
#         arr = np.delete(arr, j, 1)
#     col_sum = np.sum(arr, axis=0)
#     row_sum = np.sum(arr, axis=1)


# print(count)
