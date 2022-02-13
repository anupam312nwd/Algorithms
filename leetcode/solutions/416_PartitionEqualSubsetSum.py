#!/usr/bin/env python


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = {}
        if total % 2 == 1:
            return False
        else:
            half_total = total / 2
            num_len = len(nums)
            return self.eq_sum(nums, num_len, half_total)

    def eq_sum(nums, card, sum_val):
        if sum_val < 0:
            return False
        elif sum_val == 0:
            return True
        elif card == 0:
            return False
        elif (card, sum_val) in dp.keys():
            return dp[(card, sum_val)]
        else:
            dp[(card, sum_val)] = self.eq_sum(
                nums, card - 1, sum_val - nums[card - 1]
            ) or self.eq_sum(card - 1, sum_val)
            return dp[(card, sum_val)]
