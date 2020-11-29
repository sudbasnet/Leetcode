# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def isValidBranch(self, node, minMax):
        [minLeft, maxRight] = minMax
        if not node:
            return True
        if node.val <= minLeft or node.val >= maxRight:
            return False
        isLeftValid = self.isValidBranch(node.left, [minLeft, node.val])
        isRightValid = self.isValidBranch(node.right, [node.val, maxRight])
        return isLeftValid and isRightValid
        
    def isValidBST(self, root: TreeNode) -> bool:
        # pass minLeft and maxRight to left and right respectively
        """
        several things to think about:
        1. the left must be smaller than the parent
        2. the right musht be larger than the parent
        3. there should not be anything smaller than it self on its right
        4. there should not be anything larger than it self on its left
        
        so at each node what do I need to know???
        i need to know that the left is valid, the right is valid, 

        If I am a node, the maximum on my left should be smaller than me
        and the minimum value on my right has to be greater than me

        so at each traversal, we pass the min max bounds:
        if we go right, we just pass the maxValue we already have, and min is my current value
        if we go left then the maximum is my current value and min is passed down
        """
        return self.isValidBranch(root, [float("-inf"), float("inf")])
        
        
