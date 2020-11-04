from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        if we can find out the depth O(h) time (keep going left if there is a left)
        
        we can just check nodes that are on h-1 level
        
        2**h - (number of nodes on the right of the node with missing element + number of nodes missing in the first node with missing element)

        THERE IS A MORE EFFICIENT SOLUTION OUT THERE, I JUST COULDN'T FIGURE IT OUT IN TIME
        """
    
#       how about I do BFS and stop at the first one that has one of zero children??
        if not root:
            return 0
        
        q = Queue()
        q.put(root)
        numberOfNodes = 1 # atleast the root node needs to be there
        while not q.empty():
            currentNode = q.get()
            if currentNode.left:
                numberOfNodes += 1
                q.put(currentNode.left)
            else:
                return numberOfNodes
            if currentNode.right:
                numberOfNodes += 1
                q.put(currentNode.right)
            else:
                return numberOfNodes
        return numberOfNodes
