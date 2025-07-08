# Minimum Absolute Difference in BST - Easy
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # Inorder traversal
        diff = float('inf')
        stack: list[TreeNode] = []
        curr = root
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            diff = min(diff, abs(curr.val - prev)) if prev is not None else diff
            prev = curr.val
            curr = curr.right
        return int(diff)

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int: # DFS
        self.prev, self.diff = None, float('inf')
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev is not None:
                self.diff = min(self.diff, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return int(self.diff)
    
    def getMinimumDifference3(self, root: Optional[TreeNode]) -> int: # Morris
        diff = float('inf')
        prev, cur = None, root
        while cur:
            if not cur.left:
                diff = min(diff, cur.val - prev) if prev is not None else diff
                prev = cur.val
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    diff = min(diff, cur.val - prev) if prev is not None else diff
                    pred.right = None
                    prev = cur.val
                    cur = cur.right
        return int(diff)