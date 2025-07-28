# Find the Safest Path in a Grid - Medium
from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int: # BFS + Dijkstra v1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        n = len(grid)
        queue: deque[tuple[int, int]] = deque()
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        visited = set()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            r, c = queue.popleft()
            dist = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        dis: List[List[float]] = [[float('inf') for _ in range(n)] for _ in range(n)]
        dis[0][0] = grid[0][0]
        heap = [(-dis[0][0], 0, 0)]
        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe
            if r == n - 1 and c == n - 1:
                return int(safe)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                candidate = min(safe, grid[nr][nc])
                if dis[nr][nc] > candidate:
                    dis[nr][nc] = candidate
                    heapq.heappush(heap, (-dis[nr][nc], nr, nc))
        return int(dis[-1][-1])

    def maximumSafenessFactor2(self, grid: List[List[int]]) -> int: # BFS + Dijkstra v2
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        n = len(grid)
        queue: deque[tuple[int, int]] = deque()
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        visited = set()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            r, c = queue.popleft()
            dis = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    grid[nr][nc] = dis + 1
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        vis = [[False for _ in range(n)] for _ in range(n)]
        vis[0][0] = True
        heap = [(-grid[0][0], 0, 0)]
        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe
            if r == n - 1 and c == n - 1:
                return safe
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc]:
                    ns = min(safe, grid[nr][nc])
                    heapq.heappush(heap, (-ns, nr, nc))
                    vis[nr][nc] = True
        return -1

    def maximumSafenessFactor3(self, grid: List[List[int]]) -> int: # BFS + Dijkstra + Binary Search
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        n = len(grid)
        queue: deque[tuple[int, int]] = deque()
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        visited = set()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    queue.append((r, c))
                    visited.add((r, c))
        while queue:
            r, c = queue.popleft()
            dis = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    grid[nr][nc] = dis + 1
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        
        def has_path_with_min_safeness(min_safeness: int) -> bool:
            if grid[0][0] < min_safeness:
                return False
            visited = [[False] * n for _ in range(n)]
            dq = deque([(0, 0)])
            visited[0][0] = True
            while dq:
                y, x = dq.popleft()
                if (y, x) == (n - 1, n - 1):
                    return True
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                        if grid[ny][nx] >= min_safeness:
                            visited[ny][nx] = True
                            dq.append((ny, nx))
            return False


        low, high = 0, max(max(row) for row in grid)
        best = 0
        while low <= high:
            mid = (low + high) // 2
            if has_path_with_min_safeness(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best