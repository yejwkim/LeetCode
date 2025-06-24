# Remove Nth Node From End of List - Medium
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        cur = dummy
        while head:
            a = head
            if head.next:
                b = head.next
                cur.next = b
                cur = cur.next
                next_node = head.next.next
                head = next_node
            else:
                head = head.next
            cur.next = a
            cur = cur.next
        cur.next = None
        return dummy.next

    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]: # Optimal Solution
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            first.next = second.next
            second.next = first
            cur.next = second
            cur = first
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
        [1,2,3,4], # [2,1,4,3]
        [], # []
        [1], # [1]
        [1,2,3] # [2,1,3]
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Output:", solution.swapPairs2(head))
        print()

if __name__ == "__main__":
    main()