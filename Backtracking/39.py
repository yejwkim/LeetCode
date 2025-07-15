# Combination Sum - Medium
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if sum(path) == target:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()
        backtrack(0, [])
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path: List[int] = []
        candidates.sort()
        def backtrack(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue
                path.append(candidates[i])
                backtrack(i, remain - candidates[i])
                path.pop()
        backtrack(0, target)
        return res