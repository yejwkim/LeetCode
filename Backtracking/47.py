# Permutations II - Medium
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(start):
            if start == n:
                res.append(nums.copy())
                return
            seen = set()
            for i in range(start, n):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return res
    
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        used = [False] * n
        nums.sort()
        def backtrack(path):
            if len(path) == n:
                res.append(path.copy())
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                used[i] = False
                path.pop()
        backtrack([])
        return res