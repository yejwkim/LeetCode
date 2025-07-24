# Rotting Oranges - Medium
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        queue: deque[tuple[int, int]] = deque()
        fresh, minute = 0, -1

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0
        if not queue:
            return -1

        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minute += 1

        return minute if fresh == 0 else -1
