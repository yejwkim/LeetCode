# Design Graph With Shortest Path Calculator - Hard
from typing import List
from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf') for _ in range(self.n)]
        dist[node1] = 0
        heap: List[tuple[float, int]] = [(0, node1)]
        while heap:
            curDist, node = heapq.heappop(heap)
            if curDist > dist[node]:
                continue
            if node == node2:
                return int(curDist)
            for nei, w in self.graph[node]:
                if dist[nei] > curDist + w:
                    dist[nei] = curDist + w
                    heapq.heappush(heap, (dist[nei], nei))
        return -1
