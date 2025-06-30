# Binary Tree Postorder Traversal - Easy
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # Recursive O(n)
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]: # Iterative O(n) Two-Stack
        if not root:
            return []
        s1, s2 = [root], []
        while s1:
            node = s1.pop()
            s2.append(node.val) # will be in reverse “node → right → left”
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        return s2[::-1]

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]: # Iterative O(n) One-Stack
        res = []
        stack: List[TreeNode] = []
        last = None
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            peek = stack[-1]
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                last = stack.pop()
        return res

def build_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def print_binary_tree(root: Optional[TreeNode]):
    if not root:
        print("Empty tree")
        return
    queue = deque([(root, 0)])
    current_level = 0
    level_nodes: List[Optional[TreeNode]] = []
    while queue:
        node, level = queue.popleft()
        if level != current_level:
            print("Level", current_level, ":", level_nodes)
            level_nodes = []
            current_level = level
        level_nodes.append(node.val if node else None)
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    if level_nodes:
        print("Level", current_level, ":", level_nodes)

def main():
    test_cases = [
        [1,None,2,3], # [3,2,1]
        [1,2,3,4,5,None,8,None,None,6,7,9], # [4,6,7,5,2,9,8,3,1]
        [], # []
        [1] # [1]
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        root = build_binary_tree(values)
        print(f"Test Case {i+1}")
        print("Input (level-order):", values)
        print("Binary Tree Structure:")
        print_binary_tree(root)
        print("Output:", solution.postorderTraversal3(root))
        print()

if __name__ == "__main__":
    main()