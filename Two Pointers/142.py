# Linked List Cycle II - Medium
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

def build_linked_list(values, pos):
    dummy = ListNode()
    current = dummy
    nodes = []
    for val in values:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    if pos != -1:
        current.next = nodes[pos]  # Create the cycle
    return dummy.next

def main():
    test_cases = [
        ([3,2,0,-4], 1), # pos = 1
        ([1,2], 0), # pos = 0
        ([1], -1) # None
    ]
    solution = Solution()
    for i, (values, pos) in enumerate(test_cases):
        head = build_linked_list(values, pos)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Output:", solution.detectCycle(head))
        print()

if __name__ == "__main__":
    main()