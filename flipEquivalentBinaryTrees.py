# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        """
        THOUGHT
        -------
        Traverse each tree at the same time.
        you are always traversing the eqivalent node 
        in each tree. 
        Check the children.
        
        1. Is root1's left and right children same as root2's left and right children??
            if yes then move on
        2. Is root1's left and right children same as root2's left and right children flipped??
            if yes then flip root1's left and right
            then move on
        3. repeat
        
        fails when??
        ------------
        if current left or right does not match
        and flipped left or right also does not match
        or root1 != root2 <- this should be the first thing to check
        
        we should write a base condition 
        
        CODE
        ----
        write a function that checks the children given two roots
        if fine then call itself
        return False if any conditin fails
        
        applyFunction(left) # True or False
        applyFunction(right) # True or False
        return applyFunction(left) and applyFunction(right)
        
        """
        # helper functions
        def isLeafNode(node):
            if not node.left and not node.right:
                return True
            return False
        def leftNode(node):
            return node.left.val if node.left else None
        def rightNode(node):
            return node.right.val if node.right else None

        # edge cases
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        if root1.val != root2.val:
            return False
        
        # main cases
        
        # if reached leafnodes, but they are the same
        if root1.val == root2.val and isLeafNode(root1) and isLeafNode(root2):
            return True
        
        # if both children are the same values
        if leftNode(root1) == leftNode(root2) and rightNode(root1) == rightNode(root2):
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

        # if children have flipped values
        elif leftNode(root1) == rightNode(root2) and rightNode(root1) == leftNode(root2):
            root1.left, root1.right = root1.right, root1.left
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

        else:
            return False
        