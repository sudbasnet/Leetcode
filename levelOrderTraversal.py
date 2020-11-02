from queue import Queue

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if not root:
        return None

    # queue.put, queue.get, 
    queue = Queue()
    queue.put(root)
    sequence = []
    while not queue.empty():
        currentNode = queue.get()
        sequence.append(currentNode.val)
        if currentNode.left:
            queue.put(currentNode.left)
        if currentNode.right:
            queue.put(currentNode.right)
    print(sequence)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

levelOrderTraversal(root)