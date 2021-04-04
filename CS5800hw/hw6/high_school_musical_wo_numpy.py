#!/usr/bin/env python

import sys

# f = open("case_sample.txt", "r")
# f = open("case1.txt", "r")
# data = f.read()

data = sys.stdin.read()

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


def arr_total_sum(row_sum):
    arr_sum = 0
    for val in row_sum:
        arr_sum += val
    return arr_sum


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
        if val < ar_min and val != 0:
            arg, ar_min = i, val
    return arg, ar_min


count = 0
col_sum = arr_col_sum(arr)
row_sum = arr_row_sum(arr)

total_sum = arr_total_sum(row_sum)
# print(total_sum)

while arr_total_sum(row_sum) != 0:

    indr, row_min = arr_arg_min(row_sum)
    indc, col_min = arr_arg_min(col_sum)
    # print("row_min, col_min: ", row_min, col_min)
    # print("count: ", count)
    # print(arr)
    if row_min == float("inf"):
        break

    N = len(row_sum)

    axs, min_val = (1, row_min) if row_min <= col_min else (0, col_min)
    final_index = (-1, -1)

    if min_val == 0:
        arr_row_del(arr, indr)
        arr_col_del(arr, indc)
    else:
        min_sum = float("inf")
        if axs == 1:
            w = [i for i, val in enumerate(row_sum) if val == min_val]

            for i in w:
                temp_arr = arr[i]
                for j in range(N):
                    if temp_arr[j] == 1:
                        if min_sum > col_sum[j] and col_sum[j] != 0:
                            min_sum, final_index = col_sum[j], (i, j)

        else:
            w = [i for i, val in enumerate(col_sum) if val == min_val]
            # print("c : ", w, [col_sum[x] for x in w])

            for i in w:
                temp_arr = [arr[t][i] for t in range(N)]
                for j in range(N):
                    if temp_arr[j] == 1:
                        if min_sum > row_sum[j] and row_sum != 0:
                            min_sum, final_index = row_sum[j], (j, i)

        count += 1

        # print(axs)
        # print(i, j)
        i, j = final_index
        arr_row_del(arr, i)  # row deletion
        arr_col_del(arr, j)
    # print(count)
    # print(arr)
    # print("--------------------------------------------------")

    if len(arr[0]) == 1:
        if arr[0][0] == 1:
            count += 1
        break
    col_sum = arr_col_sum(arr)
    row_sum = arr_row_sum(arr)


print(count)
