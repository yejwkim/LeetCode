# Flood Fill - Easy
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # BFS
        if color == image[sr][sc]:
            return image

        ROWS, COLS = len(image), len(image[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        original = image[sr][sc]
        queue = deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original:
                    queue.append((nr, nc))
        return image
    
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # Iterative DFS
        if color == image[sr][sc]:
            return image

        ROWS, COLS = len(image), len(image[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        original = image[sr][sc]
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == original:
                    stack.append((nr, nc))
        return image

    def floodFill3(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]: # Recursive DFS
        if color == image[sr][sc]:
            return image

        ROWS, COLS = len(image), len(image[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        original = image[sr][sc]
        
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != original:
                return
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        dfs(sr, sc)
        return image