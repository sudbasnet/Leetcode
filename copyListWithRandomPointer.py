
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # going to use a dictionary to track all the copy nodes
        # you can use the Nodes as keys because they are also hashable
        nodes = {}
        
        # Since I might run into a node that is null, need to have a None key
        nodes = {None: None}
        
        # keeping the head as is, we will traverse using the currentNode var
        # first we will create new nodes with vals only, because I can't assign 
        #   a node to .next or .random if it's not created yet
        currentNode = head
        while currentNode:
            nodes[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next
        
        # now since one node is created per original nodes, we can assign next and random
        currentNode = head
        while currentNode:
            nodes[currentNode].next = nodes[currentNode.next]
            nodes[currentNode].random = nodes[currentNode.random]
            currentNode = currentNode.next
        
        # now just return the node which is the copy of the head node from original
        return nodes[head]