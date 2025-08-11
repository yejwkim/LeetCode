# Minimum Path Sum - Medium
from typing import List
from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: # Memoization
        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i, j):
            if i == m or j == n:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[i][j]
            return grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)

    def minPathSum2(self, grid: List[List[int]]) -> int: # Memoization
        m, n = len(grid), len(grid[0])
        memo: dict[tuple[int,int],int] = {}
        def dfs(i, j):
            if i == m or j == n:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[i][j]
            key = (i, j)
            if key in memo:
                return memo[key]
            memo[key] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))
            return memo[key]
        return dfs(0, 0)

    def minPathSum3(self, grid: List[List[int]]) -> int: # Tabulation (1D)
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = grid[0][j] + dp[j-1]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(n):
                if j > 0:
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        return dp[-1]

    def minPathSum4(self, grid: List[List[int]]) -> int: # Cleaner Tabulation (1D)
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        return int(dp[-1])