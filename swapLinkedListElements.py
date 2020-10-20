"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        since this is a singly linked list
        we need to have three elements when we are swapping values

        prev current adjacent

        current.next = adjacent.next
        adjacent.next = current
        prev.next = adjacent

        prev = prev.next.next
        """
        result = ListNode()
        result.next = head
        dummyListNode = result
        
        while dummyListNode.next and dummyListNode.next.next:
            prev = dummyListNode
            current = dummyListNode.next
            adjacent = dummyListNode.next.next
            
            current.next = adjacent.next
            adjacent.next = current
            prev.next = adjacent
            
            dummyListNode = dummyListNode.next.next
        return result.next
        