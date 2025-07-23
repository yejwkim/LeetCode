# Merge Intervals - Medium
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        cur = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            if cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
            else:
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
        res.append(cur)
        return res