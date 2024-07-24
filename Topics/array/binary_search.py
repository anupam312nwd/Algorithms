#!/usr/bin/env python


def binary_search_recur(target, arr, left, right):
    if left > right:
        return -1

    mid = int((left + right) / 2)

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recur(target, arr, mid + 1, right)
    else:
        return binary_search_recur(target, arr, left, mid - 1)


def binary_search_template(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


def binaryFind(arr, target):
    left, right = 0, len(arr) - 1
    result = right
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
        return result


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-a", "arr", "add an array")
    # parser.add_argument("-t", "target", "add a target")

    # parser.arr.sort()
    # print(binary_search(parser.val, parser.arr, 0, len(parser.arr)))

    arr = [1, 2, 2, 3, 3, 3]
    target = 3
    left = 0
    right = len(arr) - 1
    # print(binary_search_recur(target, arr, left, right))
    # print(binary_search_template(arr, target))
    print(binaryFind(arr, 2))
    print(binaryFind(arr, 3))
