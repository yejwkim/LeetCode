# Find Mode in Binary Search Tree - Easy
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev, self.count, self.max_count = None, 0, 0
        self.res: list[int] = []
        def visit(val):
            if val == self.prev:
                self.count += 1
            else:
                self.count = 1
            self.prev = val
            if self.count > self.max_count:
                self.res = [val]
                self.max_count = self.count
            elif self.count == self.max_count:
                self.res.append(val)

        cur = root
        while cur:
            if not cur.left:
                visit(cur.val)
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
                    visit(cur.val)
                    cur = cur.right
        return self.res