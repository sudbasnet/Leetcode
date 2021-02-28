# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        """ 
        preorder = root left right 
        example: [5, 2, 1, 3, 7, 6, 8]

        i can tell that 
        5 is the root, [2, 1, 3] is left and [7, 6, 8] is right

        so I could traverse through the nodes multiple times to find some thing thats larger than the root
        lets implement it first and think of the optimized solution next
        """
        # if not preorder:
        #     return None

        # node = TreeNode(preorder[0])
        # for i in range(len(preorder) + 1):
        #     # if we have looked at every item but nothing larger than root
        #     # then that means there's only left node of the root
        #     if i == len(preorder) or preorder[i] > node.val:
        #         node.left = self.bstFromPreorder(preorder[1:i])
        #         node.right = self.bstFromPreorder(preorder[i:])
        #         break
        # """
        # This solution works, alot of the nodes are being traversed repeatedly
        # lets see if we can solve this somehow ????
        # """
        # return node

        if not preorder:
            return None

        self.completed = 0
        self.preorder = preorder

        def bst(index, limit):
            if index == len(self.preorder) or preorder[index] > limit:
                self.completed = index
                return None

            node = TreeNode(self.preorder[index])
            node.left = bst(index+1, node.val)
            node.right = bst(self.completed, limit)
            return node

        return bst(0, float("inf"))
