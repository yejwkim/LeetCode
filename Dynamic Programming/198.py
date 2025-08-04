# House Robber - Medium
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int: # Memoization
        n = len(nums)
        dp = [-1] * (n)
        def maxAmount(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(maxAmount(i-1), maxAmount(i-2) + nums[i])
            return dp[i]
        return maxAmount(n-1)
    
    def rob2(self, nums: List[int]) -> int: # Tabulation
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
    
    def rob3(self, nums: List[int]) -> int: # Memory Optimized Tabulation
        a, b = 0, 0
        for num in nums:
            a, b = b, max(a + num, b)
        return b
