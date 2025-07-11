# Serialize and Deserialize BST - Medium
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values = []
        def dfs(node):
            if not node:
                return None
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "[" + ",".join(values) + "]"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data.strip("[]")
        if not data:
            return None
        preorder = deque(int(x) for x in data.split(","))
        def build(lower, upper):
            if not preorder or preorder[0] < lower or preorder[0] > upper:
                return None
            val = preorder.popleft()
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node
        return build(float('-inf'), float('inf'))