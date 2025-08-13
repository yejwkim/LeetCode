# Best Time to Buy and Sell Stock - Easy
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = float('inf')
        maxProfit = 0
        for price in prices:
            if price < l:
                l = price
            else:
                maxProfit = max(maxProfit, price - int(l))
        return maxProfit