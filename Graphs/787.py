# Cheapest Flights Within K Stops - Medium
from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: # Dijkstra; TLE
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        dis = [float('inf') for _ in range(n)]
        dis[src] = 0
        heap: List[tuple[float, int, int]] = [(0, src, k + 1)]
        while heap:
            cur_dis, node, k = heapq.heappop(heap)
            if node == dst:
                return int(cur_dis)
            if k > 0:
                for nei, w in graph[node]:
                    dis[nei] = cur_dis + w
                    heapq.heappush(heap, (dis[nei], nei, k - 1))
        return -1

    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: # BST
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue: deque[tuple[int, float]] = deque([(src, 0)])
        dis = [float('inf') for _ in range(n)]
        stops = 0

        while queue and stops <= k:
            size = len(queue)
            for i in range(size):
                node, cur_dis = queue.popleft()
                for nei, w in graph[node]:
                    if cur_dis + w >= dis[nei]:
                        continue
                    dis[nei] = cur_dis + w
                    queue.append((nei, dis[nei]))
            stops += 1
        return -1 if dis[dst] == float('inf') else int(dis[dst])