# Validate Binary Search Tree - Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # Inorder traversal
        prev = float('-inf')
        stack: list[TreeNode] = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev >= curr.val:
                return False
            prev = curr.val
            curr = curr.right
        return True

    def isValidBST2(self, root: Optional[TreeNode]) -> bool: # Bounded DFS
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float('-inf'), float('inf'))