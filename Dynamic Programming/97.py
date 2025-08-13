# Interleaving String - Medium
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool: # Memoization
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False
        memo: dict[tuple[int, int], int] = {}
        def dfs(i, j):
            k = i + j
            if i == l:
                return s2[j:] == s3[k:]
            if j == m:
                return s1[i:] == s3[k:]
            key = (i, j)
            if key in memo:
                return memo[key]
            ans = False
            if s1[i] == s3[k] and dfs(i + 1, j):
                ans = True
            if s2[j] == s3[k] and dfs(i, j + 1):
                ans = True
            memo[key] = ans
            return memo[key]
        return dfs(0, 0)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool: # Tabulation (2D)
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False
        dp = [[False] * (m + 1) for _ in range(l + 1)]
        dp[0][0] = True
        i = j = 1
        while i <= l and s1[i-1] == s3[i-1]:
            dp[i][0] = True
            i += 1
        while j <= m and s2[j-1] == s3[j-1]:
            dp[0][j] = True
            j += 1
        for i in range(1, l+1):
            for j in range(1, m+1):
                if (dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1]):
                    dp[i][j] = True
        return dp[-1][-1]

    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool: # Tabulation (1D)
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        l, m, n = len(s1), len(s2), len(s3)
        if l + m != n:
            return False
        dp = [False] * (m+1)
        dp[0] = True
        for j in range(1, m+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, l+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, m+1):
                dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        return dp[-1]