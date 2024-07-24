#!/usr/bin/env python

def monotonic_next_greater(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array)):
        while stack and array[stack[-1]] < array[i]: # monotonically decreasing
            result[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return result


def monotonic_next_smaller(array):
    stack = []
    result = [-1] * len(array)
    for i in range(len(array)):
        while stack and array[stack[-1]] > array[i]: # monotonically increasing
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
    result = [-1] * len(array)
    for i in range(len(array) - 1, -1, -1):
        while stack and array[stack[-1]] > array[i]:
            result[stack[-1]] = stack[-1] - i
            stack.pop()
        stack.append(i)
    return result


if __name__ == '__main__':
    array = [7, 3, 9, 5, 4, 2, 6]
    steps_to_next_greater = monotonic_next_greater(array)
    print(steps_to_next_greater)
    steps_to_next_smaller = monotonic_next_smaller(array)
    print(steps_to_next_smaller)
    steps_to_previous_greater = monotonic_previous_greater(array)
    print(steps_to_previous_greater)
    steps_to_previous_smaller = monotonic_previous_smaller(array)
    print(steps_to_previous_smaller)
