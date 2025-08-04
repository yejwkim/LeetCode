# House Robber III - Medium
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def robSub(node):
            if not node:
                return (0, 0)
            left = robSub(node.left)
            right = robSub(node.right)
            not_robbed = max(left[0], left[1]) + max(right[0], right[1])
            robbed = node.val + left[0] + right[0]
            return (not_robbed, robbed)
        return max(robSub(root))