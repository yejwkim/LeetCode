# K Closest Points to Origin - Medium
from typing import List
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[tuple[float, int]] = []
        for i, (x, y) in enumerate(points):
            dis = -sqrt(x * x + y * y)
            heapq.heappush(heap, (dis, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[i] for _, i in heap]