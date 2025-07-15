# Palindrome Partitioning - Medium
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]: # Only using Backtracking; O(2^n)
        def isPalindrome(word):
            return word == word[::-1]
        res = []
        def backtrack(idx, path):
            if idx == len(s):
                if isPalindrome(path[-1]):
                    res.append(path.copy())
                return None
            tmp, path[-1] = path[-1], path[-1] + s[idx]
            backtrack(idx + 1, path)
            path[-1] = tmp
            if isPalindrome(path[-1]):
                path.append(s[idx])
                backtrack(idx + 1, path)
                path.pop()
        backtrack(1, [s[0]])
        return res
    
    def partition2(self, s: str) -> List[List[str]]:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i+1][j-1]):
                    is_pal[i][j] = True
        res: List[List[str]] = []
        path: List[str] = []
        def backtrack(start: int):
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if is_pal[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return res
