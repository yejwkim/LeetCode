# Unique Paths II - Medium
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: # Memoization
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            key = (i, j)
            if key in memo:
                return memo[key]
            memo[key] = dfs(i+1, j) + dfs(i, j+1)
            return memo[key]
        return dfs(0, 0)

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int: # Tabulation (2D)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while i < m and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int: # Tabulation (1D)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]