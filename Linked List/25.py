# Reverse Nodes in k-Group - Hard
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode()
        cur = dummy
        while head:
            k_group = None
            count = 0
            while head and count < k:
                count += 1
                if count == 1:
                    group_tail = head
                next_node = head.next
                head.next = k_group
                k_group = head
                head = next_node
            if count == k:
                cur.next = k_group
                cur = group_tail
            else:
                rev = None
                while k_group:
                    next_node = k_group.next
                    k_group.next = rev
                    rev = k_group
                    k_group = next_node
                cur.next = rev
        return dummy.next

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode: # Recursion
        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next

        # Reverse the group (basic way to reverse linked list)
        prev = ListNode()
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        ([1,2,3,4,5], 2), # [2,1,4,3,5]
        ([1,2,3,4,5], 3) # [3,2,1,4,5]
    ]
    solution = Solution()
    for i, (values, k) in enumerate(test_cases):
        head = build_linked_list(values)
        print(f"Test Case {i+1}")
        print("Input linked list:", head)
        print("Input k:", k)
        print("Output:", solution.reverseKGroup2(head, k))
        print()

if __name__ == "__main__":
    main()