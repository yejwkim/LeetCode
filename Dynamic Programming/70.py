# Climbing Stairs - Easy
class Solution:
    def climbStairs(self, n: int) -> int: # Memoization
        dp = [-1] * (n + 1)
        def climb(n):
            if n <= 2:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = climb(n-1) + climb(n-2)
            return dp[n]
        return climb(n)
    
    def climbStairs2(self, n: int) -> int: # Tabulation
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs3(self, n: int) -> int: # Optimized Tabulation
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b