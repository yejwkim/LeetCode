# Edit Distance - Medium
class Solution:
    def minDistance(self, word1: str, word2: str) -> int: # Naive Recursion
        m, n = len(word1), len(word2)
        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            insert = 1 + dfs(i, j + 1)
            delete = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            return min(insert, delete, replace)
        return dfs(0, 0)

    def minDistance2(self, word1: str, word2: str) -> int: # Memoization
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
                res = dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                res = min(insert, delete, replace)
            memo[key] = res
            return memo[key]
        return dfs(0, 0)

    def minDistance3(self, word1: str, word2: str) -> int: # Tabulation (2D)
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
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    dp[i][j] = min(insert, delete, replace) + 1
        return dp[m][n]

    def minDistance4(self, word1: str, word2: str) -> int: # Tabulation (Two 1D)
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)
        prev = [j for j in range(n + 1)]
        curr = [0 for _ in range(n + 1)]
        curr[0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    insert = curr[j-1]
                    delete = prev[j]
                    replace = prev[j-1]
                    curr[j] = min(insert, delete, replace) + 1
            prev, curr = curr, prev
            curr[0] = prev[0] + 1
        return prev[n]

    def minDistance5(self, word1: str, word2: str) -> int: # Tabulation (One 1D)
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
                    insert = dp[j-1]
                    delete = dp[j]
                    replace = prev
                    dp[j] = min(insert, delete, replace) + 1
                prev = temp
        return dp[n]
