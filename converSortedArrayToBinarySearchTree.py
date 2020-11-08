# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        mid = len(nums)//2
        newNode = TreeNode(nums[mid])
        newNode.left = self.sortedArrayToBST(nums[:mid])
        newNode.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return newNode
