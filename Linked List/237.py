# Delete Node in a Linked List - Medium
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            node = node.next
    
    def deleteNode2(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next