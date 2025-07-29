# Surrounded Regions - Medium
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def dfs(r, c):
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    dfs(nr, nc)

        for c in range(COLS):
            last = ROWS - 1
            if board[0][c] == "O":
                dfs(0, c)
            if board[last][c] == "O":
                dfs(last, c)
        
        for r in range(ROWS):
            last = COLS - 1
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][last] == "O":
                dfs(r, last)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"