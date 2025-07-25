# Construct Binary Tree from Preorder and Inorder Traversal - Medium
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or len(preorder) != len(inorder):
            return None
        indexMap = {val: i for i, val in enumerate(inorder)}
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            in_root_idx = indexMap[root_val]
            left_size = in_root_idx - in_start
            root.left = build(pre_start + 1, pre_start + left_size, in_start, in_root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end, in_root_idx + 1, in_end)
            return root
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

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
        ([3,9,20,15,7], [9,3,15,20,7]), # [3,9,20,null,null,15,7]
        ([-1], [-1]) # [-1]
    ]
    solution = Solution()
    for i, (preorder, inorder) in enumerate(test_cases):
        print(f"Test Case {i+1}")
        print("Input preorder:", preorder)
        print("Input inorder:", inorder)
        print("Binary Tree Structure:")
        print_binary_tree(solution.buildTree(preorder, inorder))
        print()

if __name__ == "__main__":
    main()