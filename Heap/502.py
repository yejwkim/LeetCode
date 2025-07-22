# IPO - Hard
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap: List[tuple[int, int]] = [] # Max-Heap
        for i, profit in enumerate(profits):
            heapq.heappush(heap, (-profit, capital[i]))
        while k > 0:
            temp = []
            while heap and heap[0][1] > w:
                temp.append(heapq.heappop(heap))
            if heap:
                project = heapq.heappop(heap)
                w += -project[0]
                k -= 1
                for elem in temp:
                    heapq.heappush(heap, elem)
            else:
                k = 0
        return w

    def findMaximizedCapital2(self, k: int, w: int, profits: List[int], capital: List[int]) -> int: # Better Solution
        projects = sorted(zip(capital, profits))
        heap: List[int] = [] # Max-Heap
        i = 0
        n = len(profits)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w