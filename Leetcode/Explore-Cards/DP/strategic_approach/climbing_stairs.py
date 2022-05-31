#!/usr/bin/env python

from pyhelper import timer_wrapper


@timer_wrapper
def climb_tabulation(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(climb_tabulation(500))


@timer_wrapper
def climb_memoize(n):
    memo = {}

    def helper(i):
        if i < 2:
            return i
        if i not in memo:
            memo[i] = helper(i - 1) + helper(i - 2)
        return memo[i]

    return helper(n)


print(climb_memoize(500))
