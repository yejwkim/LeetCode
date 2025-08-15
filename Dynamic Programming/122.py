# Best Time to Buy and Sell Stock II - Medium
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: # Greedy
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total

    def maxProfit2(self, prices: List[int]) -> int: # DP
        buy = float('-inf')
        sell = 0
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, int(buy) + price)
        return sell