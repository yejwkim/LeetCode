# Copy List with Random Pointer - Medium
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional['Node']) -> Optional['Node']:
        # if not head:
        #     return None
        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     copy.next = cur.next
        #     cur.next = copy
        #     cur = copy.next
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next
        # cur, copy_head = head, head.next
        # while cur:
        #     copy = cur.next
        #     cur.next = copy.next
        #     if copy.next:
        #         copy.next = copy.next.next
        #     cur = cur.next
        # return copy_head
        return None