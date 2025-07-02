# Insert into a Binary Search Tree - Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # Recursive
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
    
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: # Iterative
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root