# Best Time to Buy and Sell Stock with Cooldown - Medium
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy = [float("-inf")] * n
        sell = [0] * n
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], int(buy[0]) + prices[1])
        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], int(buy[i-1]) + prices[i])
        return sell[-1]