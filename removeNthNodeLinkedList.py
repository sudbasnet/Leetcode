# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Since we need to do this in one pass, we will need to remember where
        each node is and number them.
        
        so we can use a dict {index: The Node}
        when we reach end we have the index so far.
        
        n = 2, 0 -> 1 -> 2 -> 3
        =======================
        we are in the program: i = 3, NodeAt(index - 1 - n).next = NodeAt(index -1 - n + 1).next
        """
        nodes = {}
        currentNode = head
        index = 0
        
        while currentNode:
            nodes[index] = currentNode
            currentNode = currentNode.next
            index += 1 # index will end up 1 more than the actual index
        
        # if i need to remove the first element, then just return head.next
        if index == n:
            return head.next
        # else: change the next of the element before the one that we are removing
        nodes[index - 1 - n].next = nodes[index - n].next
        return head
            
            