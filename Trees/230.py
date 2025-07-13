# Kth Smallest Element in a BST - Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # Inorder Traversal
        # Recursive Solution
        # res = []
        # def dfs(node):
        #     if not node:
        #         return None
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return res[k - 1]

        # Iterative Solution
        # cur, stack, res = root, [], []
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     cur = cur.right
        # return res[k - 1]

        # Morris Traversal
        cur, res = root, []
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res[k - 1]