"""
Input: a matrix with all 0s
Output: just the path at every step

[
 [1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1]
]

find the number of clusters
"""
def fetchNeighbors(matrix, coordinate): # (row, col)
    [row, col] = coordinate
    neighbors = []
    # up
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append([row - 1, col])
    # down
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append([row + 1, col])
    # left
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append([row, col - 1])
    # right
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append([row, col + 1])
    return neighbors


def numberOfClusters(matrix):
    """
    from each point, we start doing a DFS, and mark every node we visit,
    everytime we end a DFS cycle, we increase the count of clusters by 1

    Code:
    -----
    fetchNeighbors(coordinate) -> [(coordinates)] # fetchNeighbors([0, 0]) -> [[0, 1], [1, 0]]
    # furthermore, it filters out the coordinates that does not have the value of 1.
    # in above example: fetchNeighbors([0, 0]) -> [[1, 0]]

    clusters = 0
    for each point, insert neighbors into stack
    pop one out mark it as visited (make 1)
    pull its neighbors into the stack
    if no neighbors then keep popping the stack checking neighbors and marking the popped as 1
    """
    clusters = 0
    stack = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                continue
            # if the root is not zero then add to the cluster count
            clusters += 1

            stack = [[row, col]]
            while stack:
                currentNode = stack.pop()
                matrix[currentNode[0]][currentNode[1]] = 0
                neighbors = fetchNeighbors(matrix, currentNode)
                for n in neighbors: 
                    if n not in stack: 
                        stack.append(n)
    return clusters

m = [
 [1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 0, 1]
]

# expected output: 2
print(numberOfClusters(m))
# got 2, passed