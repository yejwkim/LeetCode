# Palindrome Partitioning - Medium
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        res = []
        def backtrack(idx, path):
            if idx == n:
                res.append(path.copy())
                return
            for end in range(idx, n):
                if dp[idx][end]:
                    path.append(s[idx:end+1])
                    backtrack(end+1, path)
                    path.pop()
        backtrack(0, [])
        return res