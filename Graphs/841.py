# Keys and Rooms - Medium
from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: # BFS
        queue = deque([0])
        visited = set([0])
        while queue:
            node = queue.popleft()
            for neighbor in rooms[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == len(rooms)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool: # DFS
        def dfs(node, visited):
            visited.add(node)
            for neighbor in rooms[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        visited: set[int] = set()
        dfs(0, visited)
        return len(visited) == len(rooms)