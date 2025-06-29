# Merge k Sorted Lists - Hard
from typing import Optional, List

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # O(n * k)
        if not lists:
            return None
        def mergeLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
            cur.next = list1 or list2
            return dummy.next
        k = len(lists)
        for i in range(k - 1):
            lists[i + 1] = mergeLists(lists[i], lists[i + 1])
        return lists[-1]

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # O(n log k)
        if not lists:
            return None
        return self.mergeRange(lists, 0, len(lists) - 1)
    
    def mergeRange(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.mergeRange(lists, left, mid)
        l2 = self.mergeRange(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)
    
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
            cur.next = list1 or list2
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
        [[1,4,5],[1,3,4],[2,6]], # [1,1,2,3,4,4,5,6]
        # [], # []
        # [[]], # []
        [[],[1]], # [1]
        [[3],[],[1]]
    ]
    solution = Solution()
    for i, values in enumerate(test_cases):
        lists = []
        for value in values:
            head = build_linked_list(value)
            lists.append(head)
        print(f"Test Case {i+1}")
        print("Input linked lists:", end = " ")
        for l in lists:
            print(f"{l}", end = "; ")
        print()
        print("Output:", solution.mergeKLists(lists))
        print()

if __name__ == "__main__":
    main()