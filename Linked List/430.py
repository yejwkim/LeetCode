# Flatten a Multilevel Doubly Linked List - Medium
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self._dfs(head)
        return head
    
    def _dfs(self, node):
        cur = node
        last = node
        while cur:
            nxt = cur.next
            if cur.child:
                child_tail = self._dfs(cur.child)
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None
                if nxt:
                    child_tail.next = nxt
                    nxt.prev = child_tail
                last = child_tail
            else:
                last = cur
            cur = nxt
        return last