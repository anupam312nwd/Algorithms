#!/usr/bin/env python


def findTargetSumWays(nums, S):
    # after partition, let a and b be partition sum
    # a-b = target, a+b = total, b = (total-target)/2
    # to find number of ways to obtain b if b!=a, divide by 2 if b==a
    # define dp[i] = number of ways to obtain sum b with last element as i
    # dp[i][b] = dp[k-1][b-nums[i]] sum over k from 1 to i
    # return dp[len_nums-1][b] if b != a or divide it by 2 if b == a

    # initialization: return False if (target+total)/2 is odd
    # opt[0][0] = 1

    total = sum(nums)

    if (total + S) % 2 == 1:
        return 0
    else:
        b = int((total - S) / 2)

        dp = [[0 for j in range(b + 1)] for i in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(b):
                if b - nums[i - 1] >= 0:
                    for k in range(i):
                        dp[i][j] += dp[k][b - nums[i - 1]]

        num_ways = 0
        for i in range(len(nums) + 1):
            num_ways += dp[i][b]

        print(dp)

        return num_ways


findTargetSumWays([1, 1, 1, 1, 1], 3)
