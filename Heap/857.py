# Minimum Cost to Hire K Workers - Hard
from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = sorted([w / q, q] for w, q in zip(wage, quality))
        max_heap: List[float] = []
        quality_sum = 0.0
        res = float('inf')
        for r, q in ratio:
            heapq.heappush(max_heap, -q)
            quality_sum += q
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            if len(max_heap) == k:
                res = min(res, quality_sum * r)
        return res