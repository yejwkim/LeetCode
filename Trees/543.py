# Diameter of Binary Tree - Easy
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0
        if not root:
            return 0
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.maxDiam = max(self.maxDiam, left + right)
            return max(left, right) + 1
        height(root)
        return self.maxDiam