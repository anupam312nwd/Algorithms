#!/usr/bin/env python


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def sort_range_in_place(lst):
    N = len(lst)
    for i, num in enumerate(lst):
        print(f"i: {i}, num: {num}")
        if num < N and num != lst[num]:
            print(num, lst[num])
            swap(lst[num], num, lst)
        # if num == N and i != N - 1:
        #     swap(i, num - 1, lst)
        #     while i != lst[i]:
        #         swap(i, lst[i], lst)


if __name__ == "__main__":
    lst = [8, 3, 5, 2, 4, 6, 0, 1]
    sort_range_in_place(lst)
    print(lst)
