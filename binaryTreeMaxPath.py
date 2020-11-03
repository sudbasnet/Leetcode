# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        how about we check: 
            what is the best we can get if we take a left??
            what is the best we can get if we take a right??
        
        return max(me + left + right, left + me, right + me, left, right)
        
        code:
        -----
        maxPathSum = float("-inf")
        
        max(left, right)
        you update the max at each return, and then return the left or the (right + me) to the parent
        
        took quite a few tries, would not have made it in an actual interview
        """
        if not root:
            return 0
        
        self.maxSum = float("-inf")
        def bestSum(node):
            if not node.right and not node.left:
                self.maxSum = max(self.maxSum, node.val)
                return node.val
            else:
                # since we need to compare this with the maxSum, putting -inf instead of 0
                bestRight = bestSum(node.right) if node.right else float("-inf")
                bestLeft = bestSum(node.left) if node.left else float("-inf")
                
                # missed a couple of combos, mainly the node.val alone, node.val should be returned
                # if both the left and the right summed with node.val is less than node.val
                self.maxSum = max(self.maxSum, node.val, bestRight, bestLeft, bestRight + node.val + bestLeft, bestRight + node.val, node.val + bestLeft)
                
                # if both the left and the right summed with node.val is less than node.val
                return max(node.val + bestRight, node.val + bestLeft, node.val)
            
        bestSum(root)
        return self.maxSum
        