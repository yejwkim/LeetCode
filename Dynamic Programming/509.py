# Fibonacci Number - Easy
class Solution:
    def fib(self, n: int) -> int: # Memoization
        mem = [-1] * (n + 1)
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if mem[n] != -1:
                return mem[n]
            mem[n] = dp(n-1) + dp(n-2)
            return mem[n]
        return dp(n)

    def fib2(self, n: int) -> int: # Tabulation
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fib3(self, n: int) -> int: # Better Tabulation
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a+b
        return b