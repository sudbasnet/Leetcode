class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        """
        looks like a DFS problem
        bestLength = float("-inf")
        maxSum = float("-inf")
        * start from each position
        * fetch neighbors (up, down, left, right if they exist and if they are larger than me)
        * path would be the visited array
        * add them to a stack []
        
        from every point we find multiple paths
        """
        self.pathLenth = float("-inf")
        
        def fetchNeighbors(point, grid, visited):
            neighbors = []
            [r, c] = point
            # up
            if r > 0 and grid[r-1][c] > grid[r][c] and [r-1, c] not in visited:
                neighbors.append([r-1, c])
            # down
            if r < len(grid) - 1 and grid[r+1][c] > grid[r][c] and grid[r+1][c] not in visited:
                neighbors.append([r+1, c])
            # left
            if c > 0 and grid[r][c-1] > grid[r][c] and grid[r][c-1] not in visited:
                neighbors.append([r, c-1])
            # down
            if c < len(grid[0]) - 1 and grid[r][c+1] > grid[r][c] and grid[r][c+1] not in visited:
                neighbors.append([r, c+1])
            return neighbors
        
        def findPaths(grid, pathSoFar, visited):
            currentPoint = pathSoFar[-1]
            neighbors = fetchNeighbors(currentPoint, grid, visited)
            if not neighbors:
                if self.pathLenth < len(pathSoFar):
                    self.pathLenth = len(pathSoFar)
                
            else:
                for n in neighbors:
                    findPaths(grid, pathSoFar + [n], visited + [currentPoint])
            
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                path = [[row, col]]
                visited = [[row, col]]
                findPaths(matrix, path, visited)
                    
        return self.pathLenth   

leetCode = Solution()
inputArray = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

print(leetCode.longestIncreasingPath(inputArray))