# Redundant Connection II - Hard
from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        incoming = [0] * (n + 1)

        cand1 = cand2 = None

        # Step 1: Check for a node with two parents
        for i, (u, v) in enumerate(edges):
            if incoming[v] == 0:
                incoming[v] = i + 1
            else:
                cand1 = edges[incoming[v] - 1]
                cand2 = edges[i].copy()
                edges[i][0] = edges[i][1] = -1
                break

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        # Step 2: Perform Regular Union-Find
        for u, v in edges:
            if u == -1:
                continue
            if not union(u, v): # Cycle Found
                # cand2 is invalid removal, so ans = cand1; [u, v] if not removed
                return cand1 if cand1 else [u, v]
        return cand2 if cand2 else [] # Valid Tree, so ans = cand2 or empty list if None