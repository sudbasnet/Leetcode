# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        input: 
        2 linked Lists L1 and L2, denote a number each in reverse order 432 = 2 -> 3 -> 4
        Examples: 
            123 123 -> 246
            999 999 -> 1998
            777 0 -> 777
        
        carry
        length of one could be longer than the other
        
        """
        # create two listNodes, then keep changing one's elements
        # you should not do currentNode = something, it will replace
        # the thing that currentNode is pointing at below
        # instead do currentNode.next = something
        # this will change the same element that currentNode and 
        # reversedSum is pointing at.
        currentNode = reversedSum = ListNode()
        carry = 0
        
        while l1 or l2 or carry > 0:
            currentNode.next = ListNode( ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry)%10 )
            carry = 1 if (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry >= 10 else 0
            currentNode = currentNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return reversedSum.next
        
