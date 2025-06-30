# Binary Tree Level Order Traversal - Medium
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            
        return res

def build_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def print_binary_tree(root: Optional[TreeNode]):
    if not root:
        print("Empty tree")
        return
    queue = deque([(root, 0)])
    current_level = 0
    level_nodes: List[Optional[TreeNode]] = []
    while queue:
        node, level = queue.popleft()
        if level != current_level:
            print("Level", current_level, ":", level_nodes)
            level_nodes = []
            current_level = level
        level_nodes.append(node.val if node else None)
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    if level_nodes:
        print("Level", current_level, ":", level_nodes)

def main():
    test_cases = [
        [3,9,20,None,None,15,7], # [[3],[9,20],[15,7]]
        [1], # [[1]]
        [] # []
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        root = build_binary_tree(values)
        print(f"Test Case {i+1}")
        print("Input (level-order):", values)
        print("Binary Tree Structure:")
        print_binary_tree(root)
        print("Output:", solution.postorderTraversal3(root))
        print()

if __name__ == "__main__":
    main()