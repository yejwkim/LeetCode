# Rotate List - Medium
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        counter = head
        n = 0
        while counter:
            counter = counter.next
            n += 1
        slow = fast = head
        for _ in range(k % n):
            fast = fast.next
        if slow == fast:
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = None
        res = temp
        while temp.next:
            temp = temp.next
        temp.next = head
        return res

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: # Optimal Solution
        if not head or not head.next:
            return head
        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        ([1,2,3,4,5], 2), # [4,5,1,2,3]
        ([0,1,2], 4), # [2,0,1]
        ([0,1,2], 3), # [0,1,2]
        ([1,2], 1) # [2,1]
    ]
    solution = Solution()
    for i, (values, k) in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Input k:", k)
        print("Output:", solution.rotateRight2(head, k))
        print()

if __name__ == "__main__":
    main()