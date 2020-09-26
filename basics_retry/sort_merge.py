#!/usr/bin/env python
import numpy as np

def MergeSort(lst):

    len_lst = len(lst)
    if len_lst == 1:
        return lst
    half_len = int(len_lst/2)
    lst1 = MergeSort(lst[:half_len])
    lst2 = MergeSort(lst[half_len:])
    return _merge(lst1, lst2)


def _merge(lst_a, lst_b):

    len_a = len(lst_a)
    len_b = len(lst_b)
    merged_lst = []
    i = j = 0
    while True:
        if (len_a > i) and (len_b > j):
            if lst_a[i] <= lst_b[j]:
                merged_lst.append(lst_a[i])
                i += 1
            else:
                merged_lst.append(lst_b[j])
                j += 1
        elif (len_a > i):
            return merged_lst + lst_a[i:]
        else:
            return merged_lst + lst_b[j:]


for i in range(4, 10):
    lst = list(np.random.randint(0, 777, i))
    print("--------------------------------------------------")
    print(lst)
    print(MergeSort(lst))
