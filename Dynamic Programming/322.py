# Coin Change - Medium
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: # Memoization
        memo: dict[int, int] = {}
        # memo[k] = minimum coins needed to make remainder k; -1 if impossible
        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in memo:
                return memo[remain]
            min_coin = float('inf')
            for c in coins:
                res = dfs(remain - c)
                if res >= 0:
                    min_coin = min(min_coin, res + 1)
            memo[remain] = -1 if min_coin == float('inf') else min_coin
            return memo[remain]
        return dfs(amount)

    def coinChange2(self, coins: List[int], amount: int) -> int: # Tabulation (2D)
        n = len(coins)
        dp = [[amount + 1] * (amount + 1) for _ in range(n + 1)]
        # dp[i][j] = minimum # of coins to make sum j with coins[0..i-1]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            coin = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j] # Skip
                if j >= coin: # Choose if possible
                    dp[i][j] = min(dp[i][j], dp[i][j - coin] + 1)
        return dp[n][amount] if dp[n][amount] <= amount else -1

    def coinChange3(self, coins: List[int], amount: int) -> int: # Tabulation (1D)
        n = len(coins)
        # dp[i] = minimum # of coins to make sum i
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[-1] if dp[-1] <= amount else -1