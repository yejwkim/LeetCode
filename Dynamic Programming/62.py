# Unique Paths - Medium
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: # Naive Recursion
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0, 0)

    def uniquePaths2(self, m: int, n: int) -> int: # Memoization
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 or j == n - 1:
                return 1
            key = (i, j)
            if key in memo:
                return memo[key]
            memo[key] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[key]
        return dfs(0, 0)

    def uniquePaths3(self, m: int, n: int) -> int: # Tabulation (2D)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths4(self, m: int, n: int) -> int: # Tabulation (1D)
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]