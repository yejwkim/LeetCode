# Number of Provinces - Medium
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # Union-Find
        n = len(isConnected)
        parent = list(range(n))
        rank = [0 for _ in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

        for u in range(n):
            for v in range(u + 1, n):
                if isConnected[u][v] == 1:
                    union(u, v)

        provinces = set()
        for city in parent:
            root = find(city)
            if root not in provinces:
                provinces.add(root)
        return len(provinces)

    def findCircleNum2(self, M): # BFS        
        if not M: return 0
        s = len(M)
        seen = set()
        cnt = 0
        for i in range(s):
            if i not in seen:
                q = [i]
                while q:
                    p = q.pop(0)
                    if p not in seen:
                        seen.add(p)
                        q += [k for k,adj in enumerate(M[p]) if adj and (k not in seen)]
                cnt += 1
        
        return cnt