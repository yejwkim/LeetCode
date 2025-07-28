# Swim in Rising Water - Hard
from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        heap = [(dist[0][0], 0, 0)]
        directions = ((1,0),(-1,0),(0,-1),(0,1))
        while heap:
            depth, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return int(depth)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                candidate = max(depth, grid[nr][nc])
                if dist[nr][nc] > candidate:
                    dist[nr][nc] = candidate
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))
        return int(dist[-1][-1])