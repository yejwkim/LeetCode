# Partition List - Medium
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        less_head, more_head = ListNode(), ListNode()
        less, more = less_head, more_head
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        more.next = None
        less.next = more_head.next
        return less_head.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        ([1,4,3,2,5,2], 3), # [1,2,2,4,3,5]
        ([2,1], 2) # [1,2]
    ]
    solution = Solution()
    for i, (values, x) in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Input x:", x)
        print("Output:", solution.partition(head, x))
        print()

if __name__ == "__main__":
    main()