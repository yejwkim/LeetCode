# Intersection of Two Linked Lists - Easy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        tailA = headA
        tailB = headB
        countA, countB = 1, 1
        while tailA.next:
            tailA = tailA.next
            countA += 1
        while tailB.next:
            tailB = tailB.next
            countB += 1
        if not tailA == tailB:
            return None
        pA, pB = headA, headB
        diff = abs(countA - countB)
        if countA - countB > 0:
            for _ in range(diff):
                pA = pA.next
        else:
            for _ in range(diff):
                pB = pB.next
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a

def build_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def build_intersecting_lists(listA_vals, listB_vals, skipA, skipB):
    shared = None
    tail_vals = listA_vals[skipA:]
    if tail_vals:
        shared = build_list(tail_vals)
    # Build list A
    headA = build_list(listA_vals[:skipA])
    a_tail = headA
    if a_tail:
        while a_tail.next:
            a_tail = a_tail.next
        a_tail.next = shared
    else:
        headA = shared
    # Build list B
    headB = build_list(listB_vals[:skipB])
    b_tail = headB
    if b_tail:
        while b_tail.next:
            b_tail = b_tail.next
        b_tail.next = shared
    else:
        headB = shared
    return headA, headB

def main():
    test_cases = [
        ([4,1,8,4,5], [5,6,1,8,4,5], 2, 3), # 8
        ([1,9,1,2,4], [3,2,4], 3, 1), # 2
        ([2,6,4], [1,5], 3, 2)
    ]
    solution = Solution()
    for i, (valuesA, valuesB, skipA, skipB) in enumerate(test_cases):
        headA, headB = build_intersecting_lists(valuesA, valuesB, skipA, skipB)
        print(f"Test Case {i+1}")
        print("Input linked list A:", headA)
        print("Input linked list B:", headB)
        result = solution.getIntersectionNode(headA, headB)
        print("Output:", result.val if result else "No intersection")
        print()

if __name__ == "__main__":
    main()