# Shortest Path in Binary Matrix - Medium
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        queue = deque([(0, 0, 1)])
        visited: set[tuple[int, int]] = {(0, 0)}
        directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        while queue:
            r, c, l = queue.popleft()
            if r == n - 1 and c == n - 1:
                return l
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, l + 1))
        return -1