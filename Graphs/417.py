# Pacific Atlantic Water Flow - Medium
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for i in range(ROWS):
            dfs(i, 0, pacific)
            dfs(i, COLS - 1, atlantic)
        
        for j in range(COLS):
            dfs(0, j, pacific)
            dfs(ROWS - 1, j, atlantic)

        return [list(cell) for cell in pacific & atlantic]