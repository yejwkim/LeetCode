# Count the Number of Houses at a Certain Distance I - Medium
from typing import List
from collections import defaultdict, deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0 for _ in range(n)]
        graph = defaultdict(list)
        for i in range(1, n):
            graph[i].append(i+1)
            graph[i+1].append(i)
        if abs(x - y) > 1:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(i):
            queue = deque([(i, 0)])
            visited = {i}
            while queue:
                i, dist = queue.popleft()
                if dist > 0:
                    res[dist - 1] += 1
                for nei in graph[i]:
                    if nei not in visited:
                        queue.append((nei, dist + 1))
                        visited.add(nei)
        
        for i in range(1, n + 1):
            bfs(i)
        return res