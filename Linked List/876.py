# Middle of the Linked List - Easy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        [1,2,3,4,5], # [3,4,5]
        [1,2,3,4,5,6] # [4,5,6]
    ]
    solution = Solution()
    for i, case in enumerate(test_cases):
        head = build_linked_list(case)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Output:", solution.middleNode(head))
        print()

if __name__ == "__main__":
    main()