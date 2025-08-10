# Coin Change II - Medium
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int: # Memoization
        memo: dict[tuple[int, int], int] = {}
        def dfs(idx, remain):
            if remain == 0:
                return 1
            if idx == len(coins) or remain < 0:
                return 0
            key = (idx, remain)
            if key in memo:
                return memo[key]
            take = dfs(idx, remain - coins[idx])
            skip = dfs(idx + 1, remain)
            memo[key] = take + skip
            return memo[key]
        return dfs(0, amount)

    def change2(self, amount: int, coins: List[int]) -> int: # Tabulation (2D)
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j] # Skip
                if j - coins[i-1] >= 0: # Choose
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1]

    def change3(self, amount: int, coins: List[int]) -> int: # Tabulation (1D)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1]