#!/usr/bin/env python


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def sort_range_in_place(lst):
    for i, num in enumerate(lst):
        if num != i + 1:
            swap(i, num - 1, lst)


if __name__ == "__main__":
    lst = [3, 2, 1, 5, 4]
    sort_range_in_place(lst)
    print(lst)
