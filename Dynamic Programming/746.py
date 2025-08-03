# Min Cost Climbing Stairs - Easy
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: # Memoization
        n = len(cost)
        dp = [-1] * n
        def climb(n):
            if n <= 1:
                return cost[n]
            if dp[n] != -1:
                return dp[n]
            dp[n] = min(climb(n-1), climb(n-2)) + cost[n]
            return dp[n]
        return min(climb(n-1), climb(n-2))

    def minCostClimbingStairs2(self, cost: List[int]) -> int: # Tabulation
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2])

    def minCostClimbingStairs3(self, cost: List[int]) -> int: # Space Optimized Tabulation
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)