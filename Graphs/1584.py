# Min Cost to Connect All Points - Medium
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: # Kruskal + Union Find
        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        n = len(points)
        edges = []
        for u in range(n):
            for v in range(u + 1, n):
                w = manhattan(points[u], points[v])
                edges.append((w, u, v))
        edges.sort()

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        total = 0
        path = 0
        for w, u, v in edges:
            if union(u, v):
                total += w
                path += 1
            if path == n - 1:
                break
        return total

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(points)
        graph = defaultdict(list)
        for u in range(n):
            for v in range(u + 1, n):
                w = manhattan(points[u], points[v])
                graph[u].append((v, w))
                graph[v].append((u, w))
        
        total = 0
        visited: set[int] = set()
        heap = [(0, 0)] # (dist, src)
        while len(visited) < n:
            w, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            total += w
            visited.add(idx)
            for nei, d in graph[idx]:
                if nei not in visited:
                    heapq.heappush(heap, (d, nei))
        return total