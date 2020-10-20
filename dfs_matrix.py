"""
Input: a matrix with all 0s
Output: just the path at every step
"""

def dfs(matrix):
    root = (0, 0)
    matrix[0][0] = 1
    stack = [root]
    print(stack)
    while len(stack) > 0:
        head = stack[-1] # peeking into the stack
        neighbors = fetchNeighbors(matrix, head)
        if len(neighbors) > 0:
            i, j = neighbors[0][0], neighbors[0][1]
            matrix[i][j] = 1
            stack.append((i, j))
            print(stack)
        else:
            stack.pop()

def fetchNeighbors(matrix, pt):
    neighbors = []
    i, j = pt[0], pt[1]
    if i > 0 and matrix[i - 1][j] != 1:
        neighbors.append((i-1, j))
    if j > 0 and matrix[i][j - 1] != 1:
        neighbors.append((i, j-1))
    if i < len(matrix) - 1 and matrix[i + 1][j] != 1:
        neighbors.append((i+1, j))
    if j < len(matrix[0]) - 1 and matrix[i][j + 1] != 1:
        neighbors.append((i, j+1))
    return neighbors

x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
dfs(x)