# Number of Islands - Medium
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: # DFS
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] != "1":
                return None
            grid[i][j] = "#"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

    def numIslands2(self, grid: List[List[str]]) -> int: # BFS
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "#"
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == "1":
                                grid[nx][ny] = "#"
                                queue.append((nx, ny))
        return count

    def numIslands3(self, grid: List[List[str]]) -> int: # Iterative DFS
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "#"
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == "1":
                                grid[nx][ny] = "#"
                                stack.append((nx, ny))
        return count