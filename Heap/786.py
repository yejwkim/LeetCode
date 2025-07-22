# K-th Smallest Prime Fraction - Medium
from typing import List
import heapq
from heapq import heapify, heappop, heappush

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]: # O(n^2)
        heap: List[tuple[float, int, int]] = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if len(heap) == k:
                    heapq.heappushpop(heap, (-arr[i] / arr[j], arr[i], arr[j]))
                else:
                    heapq.heappush(heap, (-arr[i] / arr[j], arr[i], arr[j]))
        res = heapq.heappop(heap)
        return [res[1], res[2]]
    
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]: # O(n + k log n)
        h = [(1 / y, 0, j + 1) for j, y in enumerate(arr[1:])]
        heapify(h)
        for _ in range(k - 1):
            _, i, j = heappop(h)
            if i + 1 < j:
                heappush(h, (arr[i + 1] / arr[j], i + 1, j))
        return [arr[h[0][1]], arr[h[0][2]]]