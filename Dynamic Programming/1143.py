# Longest Common Subsequence - Medium
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # Memoization
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            if text1[i] == text2[j]:
                res = dfs(i + 1, j + 1) + 1
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[key] = res
            return res
        return dfs(0, 0)
    
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int: # Tabulation (2D)
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int: # Tabulation (Two 1D)
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
            prev, curr = curr, prev
        return prev[m]

    def longestCommonSubsequence4(self, text1: str, text2: str) -> int: # Tabulation (One 1D)
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        return dp[m]