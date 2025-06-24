# Reverse Linked List II - Medium
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        visited = set()
        count = 0
        while current and count < 20:
            result.append(str(current.val))
            if id(current) in visited:
                result.append("(cycle)")
                break
            visited.add(id(current))
            current = current.next
            count += 1
        return " -> ".join(result)

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        index = 0
        while cur:
            if index == left - 1:
                front_tail = cur
                mid_tail = cur.next
                sub_head = cur.next
            elif index == right:
                back_head = cur.next
                cur.next = None
                break
            cur = cur.next
            index += 1
        rev_head = None
        while sub_head:
            next_nodes = sub_head.next
            sub_head.next = rev_head
            rev_head = sub_head
            sub_head = next_nodes
        front_tail.next = rev_head
        mid_tail.next = back_head
        return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        ([1,2,3,4,5,6,7], 3, 5), # [1,4,3,2,5]
        # ([5], 1, 1) # [5]
    ]
    solution = Solution()
    for i, (values, left, right) in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Input left:", left)
        print("Input right:", right)
        print("Output:", solution.reverseBetween(head, left, right))
        print()

if __name__ == "__main__":
    main()