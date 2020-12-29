# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        what we wnt to do:
        keep a counter so we know where we are. (odd or even)
        
        one head node for dummy
        in the current main list you need a prev pointer, which points to the previous node
        in the separated list, we need another prev 
        
        '''
        if not head:
            return
        
        dummyHead = dummyPrev = ListNode()
        prev = current = head
        counter = 0
        
        while current:
            counter += 1
            
            if counter%2 == 0: # even node
                # get this node out
                prev.next = current.next
                # put it in the dummy list
                dummyPrev.next = current
                dummyPrev = dummyPrev.next
            else:
                prev = current
            current = current.next
            
        dummyPrev.next = None
        prev.next = dummyHead.next
        
        return head

                