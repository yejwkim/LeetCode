# House Robber II - Medium
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int: # Memoization
        if len(nums) == 1:
            return nums[0]
        def lineRob(arr):
            n = len(arr)
            dp = [-1] * n
            def maxAmount(i):
                if i < 0:
                    return 0
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(maxAmount(i-1), maxAmount(i-2) + arr[i])
                return dp[i]
            return maxAmount(n-1)
        return max(lineRob(nums[:-1]), lineRob(nums[1:]))

    def rob2(self, nums: List[int]) -> int: # Tabulation
        if len(nums) == 1:
            return nums[0]
        def lineRob(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]
        return max(lineRob(nums[:-1]), lineRob(nums[1:]))
    
    def rob3(self, nums: List[int]) -> int: # Memory Optimized Tabulation
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        def lineRob(left, right):
            a, b = 0, 0
            for i in range(left, right):
                a, b = b, max(b, a + nums[i])
            return b
        return max(lineRob(0, n-1), lineRob(1, n))