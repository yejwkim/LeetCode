# Longest Increasing Subsequence - Medium
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int: # Memoization; TLE
        n = len(nums)
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, prev_idx):
            if i == n:
                return 0
            key = (i, prev_idx)
            if key in memo:
                return memo[key]
            best = dfs(i+1, prev_idx)
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                best = max(best, dfs(i+1, i) + 1)
            memo[key] = best
            return memo[key]
        return dfs(0, -1)

    def lengthOfLIS2(self, nums: List[int]) -> int: # Tabulation (2D)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            dp[i][0] += 1 if nums[i] > nums[0] else 0
            for j in range(1, i):
                dp[i][j] = dp[i][j-1] # Skip
                if nums[i] > nums[j]: # Use predecessor at j
                    dp[i][j] = max(dp[i][j], dp[j][j] + 1)
            dp[i][i] = dp[i][i-1]
        return max(dp[i][i] for i in range(n))

    def lengthOfLIS3(self, nums: List[int]) -> int: # Tabulation (1D)
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS4(self, nums: List[int]) -> int: # Binary Search
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x: # x can extend a subsequence of length m+1
                    i = m + 1
                else: # x is <= tails[m]; better to replace this tail
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size