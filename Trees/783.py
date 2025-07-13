# Minimum Distance Between BST Nodes - Easy
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.diff, self.prev, cur = float('inf'), None, root

        def visit(node):
            if self.prev is not None:
                self.diff = min(self.diff, node.val - self.prev)
            self.prev = node.val

        while cur:
            if not cur.left:
                visit(cur)
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    visit(cur)
                    cur = cur.right
        return int(self.diff)