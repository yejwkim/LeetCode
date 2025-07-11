# Serialize and Deserialize Binary Tree - Hard
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        res = []
        queue = deque([root])
        while queue:
            level_nodes = []
            if queue.count("null") == len(queue):
                queue.clear()
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == "null":
                    level_nodes.append("null")
                else:
                    level_nodes.append(str(node.val))
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append("null")
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append("null")
            res += level_nodes
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:len(data)-1]
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            cur = queue.popleft()
            if values[i] != "null":
                cur.left = TreeNode(int(values[i]))
                queue.append(cur.left)
            i += 1
            if i < len(values) and values[i] != "null":
                cur.right = TreeNode(int(values[i]))
                queue.append(cur.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))