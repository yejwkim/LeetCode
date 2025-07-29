# Graph Valid Tree - Medium
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: # Union-Find
        parent = list(range(n))
        rank = [0 for _ in range(n)]

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

        for u, v in edges:
            if not union(u, v):
                return False
            print(parent, rank)

        return len(set([find(i) for i in range(n)])) == 1