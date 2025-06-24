# Add Two Numbers - Medium
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = False
        while l1 and l2:
            digit_sum = l1.val + l2.val + 1 if carry else l1.val + l2.val
            carry = digit_sum // 10 == 1
            digit = digit_sum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            digit_sum = l1.val + 1 if carry else l1.val
            carry = digit_sum // 10 == 1
            digit = digit_sum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
        while l2:
            digit_sum = l2.val + 1 if carry else l2.val
            carry = digit_sum // 10 == 1
            digit = digit_sum % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(1)
        return dummy.next
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # Optimal Solution
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            digit_sum = v1 + v2 + carry
            carry = digit_sum // 10
            cur.next = ListNode(digit_sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

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
        ([2,4,3], [5,6,4]), # [7,0,8]
        ([0], [0]), # [0]
        ([9,9,9,9,9,9,9], [9,9,9,9]) # [8,9,9,9,0,0,0,1]
    ]
    solution = Solution()
    for i, (values1, values2) in enumerate(test_cases):
        head1 = build_linked_list(values1, -1)
        head2 = build_linked_list(values2, -1)
        print(f"Test Case {i+1}")
        print("Input linked list:", head1)
        print("Input linked list:", head2)
        print("Output:", solution.addTwoNumbers2(head1, head2))
        print()

if __name__ == "__main__":
    main()