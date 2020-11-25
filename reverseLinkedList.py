# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # I am going to need a previous, current and nextNode
        # have a dummy node, 
        
        """
        1 -> 2 -> 3 -> 4 -> 5 
        5 -> 4 -> 3 -> 2 -> 1
        
        step1
        pull 1 out
        2->3->4->5
        pull 2 out and put it in front of 1
        2.next = whatever's out there
        
        pull 3 out and put it infront of the last pulled
        so 3.next = whatever's out there
        
        
        """
        if not head:
            return None
        
        # partition the listnode into left and right
        # left will initially be empty 
        left = None
        # right will be the input node
        right = head
        
        # we start looking at the first node in current
        current = right
        while current:
            # save the nextnodes so we can move forward
            nextNode = current.next
            
            # pull out the first node and put it in front of whatever "left" is
            current.next = left
            left = current
            
            current = nextNode
        
        return left
        