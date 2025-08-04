# Partition Equal Subset Sum - Medium
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool: # Naive Recursion
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        def dfs(idx, remain):
            if remain == 0:
                return True
            if idx == len(nums) or remain < 0:
                return False
            if dfs(idx + 1, remain - nums[idx]): # Pick idx
                return True
            return dfs(idx + 1, remain) # Do not pick idx
        return dfs(0, target)

    def canPartition2(self, nums: List[int]) -> bool: # Memoization
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        target = total // 2
        dp = [[None] * (target + 1) for _ in range(n + 1)] # dp[i][j]: If j can be summed using elements from i to end
        def dfs(idx, remain):
            if remain == 0:
                return True
            if idx == n or remain < 0:
                return False
            if dp[idx][remain] is not None:
                return dp[idx][remain]
            # 1. Pick idx
            if dfs(idx + 1, remain - nums[idx]):
                dp[idx][remain] = True
                return True
            # 2. Do not pick idx
            dp[idx][remain] = dfs(idx + 1, remain)
            return dp[idx][remain]
        return dfs(0, target)

    def canPartition3(self, nums: List[int]) -> bool: # Tabulation
        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # 1. Skip
                dp[i][j] = dp[i-1][j]
                # 2. Pick
                if nums[i-1] <= j and dp[i-1][j - nums[i-1]]:
                    dp[i][j] = True
        return dp[n][target]

    def canPartition4(self, nums: List[int]) -> bool: # Memory Optimized Tabulation
        total = sum(nums)
        if total & 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                if dp[j - num]:
                    dp[j] = True
        return dp[target]