# The Skyline Problem - Hard
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            events.append((L, -H))
            events.append((R,  H))
        events.sort()
        res = []
        max_heap = [0]
        to_delete: dict[int, int] = defaultdict(int)
        prev = 0
        for x, h in events:
            if h < 0:
                heapq.heappush(max_heap, h)
            else:
                to_delete[-h] += 1
            while max_heap and to_delete[max_heap[0]] > 0:
                to_delete[max_heap[0]] -= 1
                heapq.heappop(max_heap)
            cur = -max_heap[0]
            if cur != prev:
                res.append([x, cur])
                prev = cur
        return res
