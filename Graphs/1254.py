# Number of Closed Islands - Medium
from typing import List
from collections import deque

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int: # Iterative BFS
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        visited = set()
        count = 0

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if grid[i][j] == 0 and (i, j) not in visited:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    isIsland = True
                    while queue:
                        r, c = queue.popleft()
                        if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                            isIsland = False
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                                queue.append((nr, nc))
                                visited.add((nr, nc))
                    if isIsland:
                        count += 1
        return count