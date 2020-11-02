# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        we keep pointers at the start of each linkedList
        if the l1.val if l1 else float("inf") <= l2.val if l2 else float("inf") 
            then add l1.val into our result.next and l1 = l1.next
        else add l2.val into our result.next and l2 = l2.next
        
        run the above while l1 or l2 is not None and then return the result
        """
        
        # edge cases: l1 or l2 is None from the beginning -> code works
        currentNode = mergedListNode = ListNode()
        while l1 or l2:
            if (l1.val if l1 else float("inf")) <= (l2.val if l2 else float("inf")):
                currentNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                currentNode.next = ListNode(l2.val)
                l2 = l2.next
            currentNode = currentNode.next
        
        return mergedListNode.next
    
        """
        examples:
        ---------
        inputs: None + None
        expected: 1 2 3 4 5
        running: 0 1 2 3 4 (5)
        """
    
    
    