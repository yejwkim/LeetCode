# Longest Palindromic Substring - Medium
class Solution:
    def longestPalindrome(self, s: str) -> str: # DP
        n = len(s)
        dp = [[False] * (n) for _ in range(n)]
        best_length = 1
        best_index = 0
        # dp[i][j] = s is palindrome from index i to j
        for i in range(n): # Length 1
            dp[i][i] = True
        for i in range(n - 1): # Length 2
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                best_length = 2
                best_index = i
        for length in range(3, n + 1): # Length 3+
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > best_length:
                        best_length = length
                        best_index = i
        return s[best_index : best_index + best_length]

    def longestPalindrome2(self, s: str) -> str: # Manacher’s Algorithm
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        dp = [0] * n
        center = right = 0
        max_len = center_idx = 0
        for i in range(1, n - 1):
            mirror = 2 * center - i # Reflected index
            if i < right: # Current index lies in the known palindrome
                dp[i] = min(right - i, dp[mirror])
            # Find the longest palindrome with i as the center
            while t[i + 1 + dp[i]] == t[i - 1 - dp[i]]:
                dp[i] += 1
            # Update center and right if new rightmost palindrome found
            if i + dp[i] > right:
                center, right = i, i + dp[i]
            # Update longest palindrome
            if dp[i] > max_len:
                max_len = dp[i]
                center_idx = i
        start = (center_idx - max_len) // 2
        return s[start : start + max_len]