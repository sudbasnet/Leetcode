"""
By starting at the top of the triangle below and moving to 
adjacent numbers on the row below, the maximum total from 
top to bottom is 23.
     3
    7 4
   2 4 6
  8 5 9 3
100 0 0 0 0 
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
               17 47 82
              18 35 87 10
             20 04 82 47 65
            19 01 23 75 03 34
           88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
       41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this 
problem by trying every route. However, Problem 67, is the same 
challenge with a triangle containing one-hundred rows; it cannot be 
solved by brute force, and requires a clever method! ;o)
"""

"""
I cant think of anything but a DFS for this problem 
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getSolution(triangle: Node):
    nodesMax = {}
    def maximumPathSum(triangle: Node):
        if triangle in nodesMax:
            return nodesMax[triangle]

        if not triangle.left and not triangle.right:
            nodesMax[triangle] = triangle.val
            return triangle.val
        maxPathSum = triangle.val + max(maximumPathSum(triangle.left), maximumPathSum(triangle.right))
        nodesMax[triangle] = maxPathSum
        return maxPathSum
    
    return maximumPathSum(triangle)

# test = Node(3)
# test.left, test.right = Node(7), Node(4)
# test.left.left = Node(2)
# test.left.right = test.right.left = Node(4)
# test.right.right = Node(6)
# test.left.left.left = Node(8)
# test.left.left.right = test.left.right.left = Node(5)
# test.left.right.right = test.right.right.left = Node(9)
# test.right.right.right = Node(3)

# print(getSolution(test))

# process the triangle
def processTriangle(triangleList):
    nodeList = [list(map(lambda x: Node(x), triangleList[i])) for i in range(len(triangleList))]
    for i in range(len(nodeList) - 1):
        parents = nodeList[i]
        children = nodeList[i + 1]

        parents[0].left = children[0]
        parents[-1].right = children[-1]

        rightChildIndex = 1
        for j in range(len(parents)-1):
            parents[j].right = parents[j+1].left = children[rightChildIndex]
            rightChildIndex += 1

    return nodeList[0][0]

question = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
triangle = processTriangle(question)
print(getSolution(triangle))

