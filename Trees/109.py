# Convert Sorted List to Binary Search Tree - Medium
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]: # O(n log n)
        if not head:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]: # O(n)
        ptr, size = head, 0
        while ptr:
            ptr = ptr.next
            size += 1
        self.cur = head
        
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            left_child = build(left, mid - 1)
            
            root = TreeNode(self.cur.val)
            root.left = left_child
            
            self.cur = self.cur.next
            root.right = build(mid + 1, right)
            return root
        return build(0, size - 1)