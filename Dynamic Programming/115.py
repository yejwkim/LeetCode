# Distinct Subsequences - Hard
class Solution:
    def numDistinct(self, s: str, t: str) -> int: # Memoization
        m, n = len(s), len(t)
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            skip = dfs(i+1, j)
            use = dfs(i+1, j+1) if s[i] == t[j] else 0
            memo[key] = skip + use
            return memo[key]
        return dfs(0, 0)

    def numDistinct2(self, s: str, t: str) -> int: # Tabulation (2D)
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def numDistinct3(self, s: str, t: str) -> int: # Tabulation (1D)
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j-1]
        return dp[-1]