# Is Graph Bipartite? - Medium
from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        
        def dfs(node, col):
            if color[node] != 0:
                return color[node] == col
            color[node] = col
            for nei in graph[node]:
                if not dfs(nei, -col):
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True

    def isBipartite2(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            if color[i] != 0:
                continue
            queue = deque([i])
            color[i] = 1
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == 0:
                        color[nei] = -color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True