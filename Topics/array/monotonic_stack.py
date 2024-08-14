#!/usr/bin/env python

def monotonic_next_greater(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array)):
        while stack and array[stack[-1]] < array[i]:  # monotonically decreasing
            result[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return result


def monotonic_next_smaller(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array)):
        while stack and array[stack[-1]] > array[i]:  # monotonically increasing
            result[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return result


def monotonic_previous_greater(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array) - 1, -1, -1):
        while stack and array[stack[-1]] < array[i]:
            result[stack[-1]] = stack[-1] - i
            stack.pop()
        stack.append(i)
    return result


def monotonic_previous_smaller(array):
    stack = []
    n = len(array)
    result = [-1] * n
    for i in range(n):
        while stack and (array[stack[-1]] >= array[i]):  # monotonic increasing
            stack.pop()
        # if stack not empty, then top of stack is previous smaller element
        if stack:
            result[i] = i - stack[-1]
        stack.append(i)
    return result


def monotonic_previous_smaller_reverse(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array) - 1, -1, -1):
        while stack and array[stack[-1]] > array[i]:
            result[stack[-1]] = stack[-1] - i
            stack.pop()
        stack.append(i)
    return result


def monotonicTest():
    array = [7, 3, 9, 5, 4, 2, 6]
    next_greater = [2, 1, -1, 3, 2, 1, -1]
    next_smaller = [1, 4, 1, 1, 1, -1, -1]
    previous_greater = [-1, 1, -1, 1, 1, 1, 4]
    previous_smaller = [-1, -1, 1, 2, 3, -1, 1]
    assert monotonic_next_smaller(array) == next_smaller
    assert monotonic_next_greater(array) == next_greater
    assert monotonic_previous_smaller(array) == previous_smaller
    assert monotonic_previous_smaller_reverse(array) == previous_smaller
    assert monotonic_previous_greater(array) == previous_greater
    print("all test cases passed!")


if __name__ == '__main__':
    monotonicTest()
