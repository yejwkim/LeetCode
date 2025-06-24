# Merge Two Sorted Lists - Easy
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
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
        ([1,2,4], [1,3,4]), # [1,1,2,3,4,4]
        ([], []), # []
        ([], [0]) # [0]
    ]
    solution = Solution()
    for i, (values1, values2) in enumerate(test_cases):
        head1 = build_linked_list(values1)
        head2 = build_linked_list(values2)
        print(f"Test Case {i+1}")
        print("Input linked list:", head1)
        print("Input linked list:", head2)
        print("Output:", solution.mergeTwoLists(head1, head2))
        print()

if __name__ == "__main__":
    main()