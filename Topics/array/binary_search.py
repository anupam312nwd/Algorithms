#!/usr/bin/env python


def binary_search(val, arr, left, right):
    if left > right:
        return -1

    mid = int((left + right) / 2)

    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return binary_search(val, arr, mid + 1, right)
    else:
        return binary_search(val, arr, left, mid - 1)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-a", "arr", "add an array")
    # parser.add_argument("-t", "target", "add a target")

    # parser.arr.sort()
    # print(binary_search(parser.val, parser.arr, 0, len(parser.arr)))

    arr = [1, 2]
    val = 2
    left = 0
    right = len(arr) - 1
    print(binary_search(val, arr, left, right))
