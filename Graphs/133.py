# Clone Graph - Medium
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: # BFS
        if not node:
            return None
        queue = deque([node])
        copies = {node.val: Node(node.val, [])}
        while queue:
            cur = queue.popleft()
            cur_copy = copies[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in copies:
                    copies[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cur_copy.neighbors.append(copies[neighbor.val])
        return copies[node.val]

    def cloneGraph2(self, node: 'Node') -> 'Node': # DFS
        old_to_new: dict['Node', 'Node'] = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy 
        
        return clone(node) if node is not None else None