# Best Time to Buy and Sell Stock IV - Hard
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("-inf")] * k
        sell = [0] * k
        for p in prices:
            for i in range(k):
                buy[i] = max(buy[i], sell[i-1] - p) if i != 0 else max(buy[0], -p)
                sell[i] = max(sell[i], int(buy[i]) + p)
        return sell[-1]

    def maxProfit2(self, k: int, prices: List[int]) -> int: # Optimized Version
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        k = min(k, n // 2)
        if k == n // 2: # Unlimited Transactions
            total = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    total += prices[i] - prices[i-1]
            return total

        buy = [float("-inf")] * k
        sell = [0] * k
        for p in prices:
            for i in range(k):
                buy[i] = max(buy[i], sell[i-1] - p) if i != 0 else max(buy[0], -p)
                sell[i] = max(sell[i], int(buy[i]) + p)
        return sell[-1]