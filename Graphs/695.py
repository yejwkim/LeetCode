# Max Area of Island - Medium
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        visited = set()
        maxArea = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    area = 0
                    while queue:
                        area += 1
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                    maxArea = max(maxArea, area)
        return maxArea