class Solution:
    def numIslands(self, grid) -> int:
        """
        this is pretty easy, all you need to do is a DFS from each pointer
        while doing DFS, change the explored point to 0 so we dont check it again
        
        code
        ----
        islands = 0
        for row
            for col
                put the row col in stack
                while stack is not empty:
                    pop stack
                    grab neighbors and put into stack
                
                everytime a while loop ends means we are out of neighbors 
                that are 1, so we increase the count of islands by 1 and move on
        """
        def fetchNeighbors(coordinate, matrix):
            [row, col] = coordinate
            neighbors = []
            # up
            if row > 0 and matrix[row - 1][col] == "1":
                neighbors.append([row - 1, col])
            # down
            if row < len(matrix) - 1 and matrix[row + 1][col] == "1":
                neighbors.append([row + 1, col])
            # left
            if col > 0 and matrix[row][col-1] == "1":
                neighbors.append([row, col-1])
            # right
            if col < len(matrix[0]) - 1 and matrix[row][col + 1] == "1":
                neighbors.append([row, col + 1])
            return neighbors
            
        counter = 0
        stack = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    stack.append([row, col])
                    counter += 1
                while stack:
                    [currentRow, currentCol] = stack.pop()
                    grid[currentRow][currentCol] = 0
                    neighbors = fetchNeighbors([currentRow, currentCol], grid)
                    # fetchNeighbors returns up, down, left, right if they exist and are 1
                    stack += neighbors
        return counter
                    
                