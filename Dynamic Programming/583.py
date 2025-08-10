# Delete Operation for Two Strings - Medium
class Solution:
    def minDistance(self, word1: str, word2: str) -> int: # Tabulation (2D)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]

    def minDistance2(self, word1: str, word2: str) -> int: # Tabulation (Two 1D)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        curr[0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(curr[j-1], prev[j]) + 1
            curr, prev = prev, curr
            curr[0] = prev[0] + 1
        return prev[n]

    def minDistance3(self, word1: str, word2: str) -> int: # Tabulation (One 1D)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j-1], dp[j]) + 1
                prev = temp
        return dp[n]

    def minDistance4(self, word1: str, word2: str) -> int: # Memoization
        m, n = len(word1), len(word2)
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            key = (i, j)
            if key in memo:
                return memo[key]
            if word1[i] == word2[j]:
                memo[key] = dfs(i + 1, j + 1)
            else:
                memo[key] = 1 + min(dfs(i + 1, j), dfs(i, j + 1))
            return memo[key]
        return dfs(0, 0)