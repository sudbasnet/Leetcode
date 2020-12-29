'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
'''

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        looks like an inorder traversal.
        
        the left most node shoud have the head
        and since we need to return that node, we need to set it up as the root node.
        
        put all the nodes in an array, then udpate their right and left.
        
        then return the first element in the array
        '''
        # iterative inorder traversal
        
        # put nodes in a stack when you are going down
        # the prev = stack.pop()
        # basically do a dfs always printing left self right
        # and before you pop then, change their left and right
        if not root:
            return None
        
        stack = [root]
        visited = {root: True}
        prev = head = Node()
        while stack:
            current = stack[-1]
            if current.left and current.left not in visited:
                stack.append(current.left)
            else:
                # pop yourself out
                current = stack.pop()
                visited[current] = True
                # add to previous
                current.left = prev
                prev.right = current
                prev = prev.right
                
                # now check for the right branch
                if current.right and current.right not in visited:
                    stack.append(current.right)
                    
        prev.right = head.right
        prev.right.left = prev

        return head.right
            
        