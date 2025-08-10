# Target Sum - Medium
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int: # Naive Recursion
        def dfs(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            return dfs(idx + 1, total + nums[idx]) + dfs(idx + 1, total - nums[idx])
        return dfs(0, 0)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int: # Memoization
        # memo[(i, total)] = number of ways from idx i with running sum = total
        memo: dict[tuple[int, int],int] = {}
        def dfs(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0
            key = (idx, total)
            if key in memo:
                return memo[key]
            count_plus = dfs(idx + 1, total + nums[idx])
            count_minus = dfs(idx + 1, total - nums[idx])
            memo[key] = count_plus + count_minus
            return memo[key]
        return dfs(0, 0)

    def findTargetSumWays3(self, nums: List[int], target: int) -> int: # Tabulation
        S = sum(nums)
        if S < abs(target) or (S + target) % 2 != 0:
            return 0
        # Find the number of subsets that sums to P
        P = (S + target) // 2
        n = len(nums)
        dp = [[0] * (P + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1): # Iterate over nums
            for j in range(P + 1):
                # Skip
                dp[i][j] = dp[i-1][j]
                # Choose
                if nums[i-1] <= j:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
        return dp[n][P]

    def findTargetSumWays4(self, nums: List[int], target: int) -> int: # Space Optimized Tabulation
        S = sum(nums)
        if S < abs(target) or (S + target) % 2 != 0:
            return 0
        # Find the number of subsets that sums to P
        P = (S + target) // 2
        n = len(nums)
        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]