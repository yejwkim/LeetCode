# Unique Paths III - Hard
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        ROWS, COLS = len(grid), len(grid[0])
        empty_square = 0
        r, c = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    r, c = i, j
                if grid[i][j] == 0:
                    empty_square += 1
        def backtrack(r, c, remain):
            if grid[r][c] == 2:
                if remain == 0:
                    self.res += 1
                return
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                ndr, ndc = r + dr, c + dc
                if (0 <= ndr < ROWS and 0 <= ndc < COLS):
                    if grid[ndr][ndc] == 0:
                        grid[ndr][ndc] = -1
                        backtrack(ndr, ndc, remain - 1)
                        grid[ndr][ndc] = 0
                    elif grid[ndr][ndc] == 2:
                        backtrack(ndr, ndc, remain)
        backtrack(r, c, empty_square)
        return self.res

    def uniquePathsIII2(self, grid: List[List[int]]) -> int:
        self.res = 0
        ROWS, COLS = len(grid), len(grid[0])
        walkable = 0
        r, c = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    r, c = i, j
                if grid[i][j] != -1:
                    walkable += 1
        def backtrack(r, c, remain):
            if grid[r][c] == 2:
                if remain == 1:
                    self.res += 1
                return
            temp, grid[r][c] = grid[r][c], -1
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                ndr, ndc = r + dr, c + dc
                if (0 <= ndr < ROWS and 0 <= ndc < COLS) and grid[ndr][ndc] != -1:
                    backtrack(ndr, ndc, remain - 1)
            grid[r][c] = temp
        backtrack(r, c, walkable)
        return self.res