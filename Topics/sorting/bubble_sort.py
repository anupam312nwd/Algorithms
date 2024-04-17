#!/usr/bin/env python


def bubble_sort(nums):
    n = len(nums)
    for k in range(1, n):
        isSorted = True
        print(k, nums)
        for i in range(n-k):
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                isSorted = False
        if isSorted:
            break
    return nums

if __name__ == '__main__':
    nums = [7, 5, 6, 3, 8, 9, 11, 12]
    sorted_nums = bubble_sort(nums)
    print(sorted_nums)
