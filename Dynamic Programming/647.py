# Palindromic Substrings - Medium
class Solution:
    def countSubstrings(self, s: str) -> int: # DP
        n = len(s)
        count = n
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        return count

    def countSubstrings2(self, s: str) -> int: # Reduced Space
        n = len(s)
        dp = [False] * n
        count = 0
        for i in range(n-1, -1, -1):
            prev = False # dp[j-1]
            for j in range(i, n):
                temp = dp[j]
                if s[i] == s[j] and (j - i < 2 or prev):
                    dp[j] = True
                    count += 1
                else:
                    dp[j] = False
                prev = temp
        return count

    def countSubstrings3(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
    
    def countSubstrings4(self, s: str) -> int: # Manacher
        n = len(s)
        if n == 0:
            return 0
        # d1[i] = radius (# of chars) of the longest odd-length palindrome centered at i
        d1 = [0] * n
        l = r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        # d2[i] = radius for even-length palindrome centered between i-1 and i
        d2 = [0] * n
        l = r = -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1
        # total palindromic substrings = sum of all odd radii + sum of all even radii
        return sum(d1) + sum(d2)