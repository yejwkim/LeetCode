# Best Time to Buy and Sell Stock III - Hard
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for p in prices:
            buy1 = max(buy1, -p) # rest or buy (sell0 - p = -p)
            sell1 = max(sell1, int(buy1) + p) # rest or sell
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, int(buy2) + p)
        return sell2