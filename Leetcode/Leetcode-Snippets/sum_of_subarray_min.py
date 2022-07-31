#!/usr/bin/env python


def sumSubarrayMins2(arr) -> int:

    M = 10 ** 9 + 7
    sums = 0
    arr.append(0)  # Sentinel value to pop all elements off the stack
    stack = [-1]

    for i2, num in enumerate(arr):
        # Mantain a monotone increasing stack
        while len(stack) > 1 and num < arr[stack[-1]]:
            index = stack.pop()
            left = index - stack[-1]
            right = i2 - index
            sums += right * left * arr[index]
        stack.append(i2)

    return sums % M


def sumSubarrayMins(arr):
    stack = [-1]
    result = 0
    for idx, x in enumerate(arr + [0]):
        while len(stack) > 1 and x < arr[stack[-1]]:
            index = stack.pop()
            left_length = index - stack[-1]
            right_length = idx - index
            result += left_length * right_length * arr[index]
        stack.append(idx)
    return result % (10 ** 9 + 7)


if __name__ == "__main__":
    arr = [1, 5, 3, 4, 2]
    total = sumSubarrayMins(arr)
    print(total)
    total = sumSubarrayMins2(arr)
    print(total)
