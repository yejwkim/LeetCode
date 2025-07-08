# Delete Node in a BST - Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: # Recursive
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left: # No left child
                return root.right
            if not root.right: # No right child
                return root.left
            successor = root.right # Both children
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: # Iterative
        def findMin(node):
            parent = None
            while node:
                parent, node = node, node.left
            return parent, node

        dummy = TreeNode(0)
        dummy.left = root
        parent, node = dummy, root
        
        while node and node.val != key:
            parent = node
            node = node.left if key < node.val else node.right
        
        if not node:
            return dummy.left
        
        if not node.left or not node.right: # One or no children
            child = node.left if node.left else node.right
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child
        else: # Two children
            succ_parent, succ = findMin(node.right)
            node.val = succ.val
            if succ_parent:
                succ_parent.left = succ.right
            else:
                node.right = succ.right

        return dummy.left