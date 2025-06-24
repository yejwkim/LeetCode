# Palindrome Linked List - Easy
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return False

def buildLinkedList(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def main():
    test_cases = [
        [1,2,2,1], # true
        [1,2], # false
        [1,2,3,4,3,2,1],
        [1,2,3,3,2,1]
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        head = buildLinkedList(values)
        print(f"Test Case {i+1}")
        print("Input head:", head)
        print("Output:", solution.isPalindrome(head))
        print()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
        #     if head is None:
        #     return False
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # prev = None
        # while slow:
        #     next_temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = next_temp
        # left, right = head, prev
        # while right:
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next
        # return True