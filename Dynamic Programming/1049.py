# Last Stone Weight II - Medium
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int: # Tabulation
        total = sum(stones)
        maxTotal = total // 2
        print(maxTotal)
        n = len(stones)
        dp = [[False] * (maxTotal + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(maxTotal + 1):
                dp[i][j] = dp[i-1][j] # Skip
                if stones[i-1] <= j and dp[i-1][j-stones[i-1]]:
                    dp[i][j] = True # Choose if possible
        for i in range(maxTotal, -1, -1):
            if dp[-1][i]:
                return total - 2 * i
        return -1

    def lastStoneWeightII2(self, stones: List[int]) -> int: # Space Optimized Tabulation
        total = sum(stones)
        maxTotal = total // 2
        dp = [False] * (maxTotal + 1)
        dp[0] = True
        for num in stones:
            for j in range(maxTotal, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        for i in range(maxTotal, -1, -1):
            if dp[i]:
                return total - 2 * i
        return -1

    def lastStoneWeightII3(self, stones: List[int]) -> int: # Memoization
        memo: dict[tuple[int, int], int] = {}
        total = sum(stones)
        maxTotal = total // 2
        def dfs(idx, count):
            if idx == len(stones):
                return count
            key = (idx, count)
            if key in memo:
                return memo[key]
            best = dfs(idx + 1, count) # skip
            if stones[idx] + count <= maxTotal:
                best = max(best, dfs(idx + 1, count + stones[idx]))
            memo[key] = best
            return best
        return total - 2 * dfs(0, 0)