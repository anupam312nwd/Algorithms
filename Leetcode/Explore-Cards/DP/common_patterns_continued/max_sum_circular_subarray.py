class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # DP
        # if not circular
        # dp[i] = max sum ending at index i
        # dp[i] = max(dp[i-1]+nums[i], nums[i])
        # base-case: dp[0] = nums[0]
        # result = max(dp)
        # use above in both directions

        n = len(nums)
        prefix_sum = [0] * n
        max_suffix_sum = [0] * n
        max_subarray_sum = [0] * n

        max_subarray_sum[0] = nums[0]
        prefix_sum[0] = nums[0]

        for i in range(1, n):
            max_subarray_sum[i] = max(max_subarray_sum[i - 1] + nums[i], nums[i])
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix_sum = nums[i]
                max_suffix_sum[i] = nums[i]
            else:
                suffix_sum = suffix_sum + nums[i]
                max_suffix_sum[i] = max(max_suffix_sum[i + 1], suffix_sum)

        special_sum = [0] * n
        for i in range(n - 1):
            special_sum[i] = prefix_sum[i] + max_suffix_sum[i + 1]
        special_sum[n - 1] = prefix_sum[n - 1]

        result = -float("inf")
        for i in range(n):
            result = max(result, special_sum[i], max_subarray_sum[i])
        return result

# TC: O(n)
# SC: O(n)
