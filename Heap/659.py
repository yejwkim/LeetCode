# Split Array into Consecutive Subsequences - Medium
from typing import List
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        unused = Counter(nums)
        end: Counter[int] = Counter()
        for i in nums:
            if not unused[i]:
                continue
            unused[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif unused[i + 1] and unused[i + 2]:
                unused[i + 1] -= 1
                unused[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True