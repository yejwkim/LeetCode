# Course Schedule II - Medium
from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: # BFS (Khan)
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
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

        return res if len(res) == numCourses else []

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: # DFS
        graph = defaultdict(list)
        visited = [0] * numCourses
        res = []
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
            res.append(node)
            return True
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]