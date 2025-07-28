# Course Schedule - Medium
from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # DFS
        # -1 = visiting; 1 = visited; 0 = not visited
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # BFS (Kahn's)
        graph = defaultdict(list)
        indegree = [0] * numCourses
        res = []
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque([i for i, elem in enumerate(indegree) if elem == 0])
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return len(res) == numCourses