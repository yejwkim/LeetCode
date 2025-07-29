# Connecting Cities With Minimum Cost - Medium
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimum_cost(self, n: int, connections: List[List[int]]) -> int: # Kruskal + Union-Find
        edges = [(w, u, v) for u, v, w in connections]
        edges.sort()
        parent = list(range(n+1))
        rank = [0] * (n+1)

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
        
        total = 0
        components = n
        
        for w, u, v in edges:
            if union(u, v):
                total += w
                components -= 1
                if components == 1:
                    break

        return total if components == 1 else -1

    def minimum_cost2(self, n: int, connections: List[List[int]]) -> int: # Prim + Min-Heap
        graph = defaultdict(list)
        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = [False] * (n + 1)
        total = 0
        components = 0
        for i in range(1, n + 1):
            if visited[i]:
                continue
            components += 1
            if components > 1:
                return -1
            heap = [(0, i)]
            while heap:
                w, idx = heapq.heappop(heap)
                if visited[idx]:
                    continue
                visited[idx] = True
                total += w
                for nei, d in graph[idx]:
                    if not visited[nei]:
                        heapq.heappush(heap, (d, nei))
        return total if components == 1 else -1

def main():
    solution = Solution()
    test_cases = [
        (3, [[1,2,1], [2,3,2], [1,3,3]]), # 3
        (3, [[1,2,1]]) # -1
    ]
    
    for i, (n, connections) in enumerate(test_cases):
        print(f"Test Case {i+1}:")
        print(f"Input n: {n}")
        print(f"Input connections: {connections}")
        print(f"Output: {solution.minimum_cost2(n, connections)}")
        print()

if __name__ == "__main__":
    main()