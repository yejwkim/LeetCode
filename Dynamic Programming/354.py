# Russian Doll Envelopes - Hard
from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int: # Tabulation (2D)
        envelopes.sort()
        n = len(envelopes)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                skip = dp[i+1][j]
                use = 0
                if j == 0 or (envelopes[i][0] > envelopes[j-1][0] and envelopes[i][1] > envelopes[j-1][1]):
                    use = dp[i+1][i+1] + 1
                dp[i][j] = max(skip, use)
        return dp[0][0]

    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int: # Tabulation (1D)
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n
        for i in range(n):
            w, h = envelopes[i]
            for j in range(i):
                pw, ph = envelopes[j]
                if w > pw and h > ph:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def maxEnvelopes3(self, envelopes: List[List[int]]) -> int: # Binary Search
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        tails: List[int] = []
        for _, h in envelopes:
            if not tails or h > tails[-1]:
                tails.append(h)
            else:
                l, r = 0, len(tails)
                while l != r:
                    m = (l + r) // 2
                    if tails[m] < h:
                        l = m + 1
                    else:
                        r = m
                tails[l] = h
        return len(tails)

    def maxEnvelopes4(self, envelopes: List[List[int]]) -> int: # Binary Search
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        tails: List[int] = []
        for _, h in envelopes:
            k = bisect_left(tails, h)
            if k == len(tails):
                tails.append(h)
            else:
                tails[k] = h
        return len(tails)