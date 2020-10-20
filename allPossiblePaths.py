"""
input number of rows and cols for the phone pattern
start, left, .....
start, right, .......

x x 
x x

"""
from copy import deepcopy

def allPossiblePaths(matrix, point, path = [], visited = []):
    i, j = point[0], point[1]
    visited.append((i, j))
    path.append((i, j))
    print(path)
    neighbors = fetchNeighbors(deepcopy(matrix), (i,j), deepcopy(visited))
    if len(neighbors) == 0:
        return
    for n in neighbors:
        allPossiblePaths(matrix, n, deepcopy(path), deepcopy(visited))

def fetchNeighbors(matrix, pt, visited):
    neighbors = []
    for diff in [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]:
        # (-1, 1) (-1,0) ...
        i, j = diff[0], diff[1]
        if 0 <= pt[0] + i <= len(matrix) - 1 and 0 <= pt[1] + j <= len(matrix[0]) -1 and (pt[0]  + i, pt[1] + j) not in visited:
            neighbors.append((pt[0]  + i, pt[1] + j) )
    return neighbors


mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
allPossiblePaths(mat, (0, 0))