# Remove Zero Sum Consecutive Nodes from Linked List - Medium
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
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        cur, prefix = dummy, 0
        prefix_map = {}
        while cur:
            prefix += cur.val
            prefix_map[prefix] = cur
            cur = cur.next
        cur, prefix = dummy, 0
        while cur:
            prefix += cur.val
            cur.next = prefix_map[prefix].next
            cur = cur.next
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
        [1,2,-3,3,1], # [3,1]
        [1,2,3,-3,4], # [1,2,4]
        [1,2,3,-3,-2], # [1]
        [0] # []
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Output:", solution.removeZeroSumSublists(head))
        print()

if __name__ == "__main__":
    main()