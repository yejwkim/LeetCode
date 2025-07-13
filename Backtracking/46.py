# Permutations - Medium
from typing import List

class Solution:
    # Approach 1: Slicing O(n^2 * n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, remain):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i, elem in enumerate(remain):
                path.append(elem)
                new_remain = remain[:i] + remain[i + 1:] # This is O(n), so we must avoid this
                backtrack(path, new_remain)
                path.pop()
        backtrack([], nums)
        return res
    
    # Approach #2: In-place Swap O(n * n!)
    def permute2(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def backtrack(start):
            if start == n:
                res.append(nums.copy())
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res

    # Approach #3: Used Array O(n * n!)
    def permute3(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        used = [False] * n
        path: List[int] = []
        def backtrack():
            if len(path) == n:
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return res