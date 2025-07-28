# Path With Minimum Effort - Medium
from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        efforts = {(r, c): float('inf') for c in range(COLS) for r in range(ROWS)}
        efforts[(0, 0)] = 0
        heap: List[tuple[float, int, int]] = [(0, 0, 0)]
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        while heap:
            effort, r, c = heapq.heappop(heap)
            if effort > efforts[(r, c)]:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return int(effort)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                diff = max(efforts[(r, c)], abs(heights[nr][nc] - heights[r][c]))
                if efforts[(nr, nc)] > diff:
                    efforts[(nr, nc)] = diff
                    heapq.heappush(heap, (efforts[(nr, nc)], nr, nc))
        return int(efforts[(ROWS - 1, COLS - 1)])