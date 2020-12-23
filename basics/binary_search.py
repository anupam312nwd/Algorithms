#!/usr/bin/env python

# import argparse


def binary_search(val, arr, sind, eind):
    if sind > eind:
        return -1

    mind = int((sind + eind) / 2)

    if arr[mind] == val:
        return mind
    elif arr[mind] < val:
        return binary_search(val, arr, mind + 1, eind)
    else:
        return binary_search(val, arr, sind, mind - 1)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-a", "arr", "add an array")
    # parser.add_argument("-t", "target", "add a target")

    # parser.arr.sort()
    # print(binary_search(parser.val, parser.arr, 0, len(parser.arr)))

    arr = [1, 2]
    val = 2
    sind = 0
    eind = len(arr) - 1
    print(binary_search(val, arr, sind, eind))
