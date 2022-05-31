#!/usr/bin/env python

from functools import lru_cache


def robber_lru(nums):
    @lru_cache(100)
    def helper(nums):
        if len(nums) < 3:
            return max(nums)
        return max(helper(nums[:-2]) + nums[-1], helper(nums[:-1]))

    print(helper)
    return helper(nums)


def robber_memo(nums):
    memo = {}

    def helper(i):
        if i < 2:
            return max(nums[: i + 1])
        if i not in memo:
            memo[i] = max(helper(i - 1), helper(i - 2) + nums[i])
        return memo[i]

    return helper(len(nums) - 1)


def robber_memo_down(nums):
    memo = {}
    n = len(nums)

    def helper(i):
        if n - i < 2:
            return max(nums[: n - i + 1])
        if i not in memo:
            memo[i] = max(helper(i + 2) + nums[n - i], helper(i + 1))
        return memo[i]

    helper(1)
    return memo[1]


if __name__ == "__main__":
    # result = robber_lru([17, 1, 2, 19])
    result = robber_lru((17, 1, 2, 19))
    print(f"result: {result}")
    print("--------------------------------------------------")
    result = robber_memo_down((17, 1, 2, 19))
    print(f"result: {result}")
    print("--------------------------------------------------")
    result = robber_memo((17, 1, 2, 19))
    print(f"result: {result}")
