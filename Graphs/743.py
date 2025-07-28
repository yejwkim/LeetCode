# Network Delay Time - Medium
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = [float('inf') for _ in range(n)]
        dis[k-1] = 0
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u-1].append((v-1, t))
        heap: List[tuple[float, int]] = [(0, k-1)]
        while heap:
            curDis, node = heapq.heappop(heap)
            if curDis > dis[node]:
                continue
            for nei, w in graph[node]:
                if dis[nei] > curDis + w:
                    dis[nei] = curDis + w
                    heapq.heappush(heap, (dis[nei], nei))
        res = max(dis)
        return int(res) if max(dis) != float('inf') else -1