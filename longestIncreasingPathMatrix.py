class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        """
        looks like a DFS problem
        bestLength = float("-inf")
        maxSum = float("-inf")
        * start from each position
        * fetch neighbors (up, down, left, right if they exist and if they are larger than me)
        * path would be the visited array
        * add them to a stack []

        from every point we find multiple paths
        we also need to store what is the longest path from any of my neighbors

        so the ans for longest path from current node is maxPath(neighbors) + 1
        """

        '''
        if I have no neighbors return 1
        else return 1 + max(my neighbor's max path)
        '''
        self.matrix = matrix
        maxPathLength = 0
        self.pathLengths = {}

        def getNeighbors(point):
            (r, c) = point
            neighbors = []
            if r > 0 and self.matrix[r-1][c] > self.matrix[r][c]:
                neighbors.append((r-1, c))
            if c > 0 and self.matrix[r][c-1] > self.matrix[r][c]:
                neighbors.append((r, c-1))
            if r < len(self.matrix) - 1 and self.matrix[r+1][c] > self.matrix[r][c]:
                neighbors.append((r+1, c))
            if c < len(self.matrix[0]) - 1 and self.matrix[r][c+1] > self.matrix[r][c]:
                neighbors.append((r, c+1))
            return neighbors

        def pathLength(point):
            if point in self.pathLengths:
                return self.pathLengths[point]
            neighbors = getNeighbors(point)
            maxPath = 0
            for neighbor in neighbors:
                maxPath = max(maxPath, pathLength(neighbor))
            self.pathLengths[point] = 1 + maxPath
            return 1 + maxPath

        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                if (r, c) in self.pathLengths:
                    maxPathLength = max(
                        maxPathLength, self.pathLengths[(r, c)])
                else:
                    maxPathLength = max(maxPathLength, pathLength((r, c)))

        return maxPathLength
