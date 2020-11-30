class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        """
        The idea is to do a dynamic programming, starting left top we go row by row
        and store the largest triangle that ends at each cell.
        
        so we can go through each cell [row, col] and get the min of [row-1, col], [row, col-1], [row-1, col-1]
        and add 1 to it. Note that we just skip if the current cell has value 0
        
        
        """
        # keep the maxval
        # start two for loops for row and col
        # update the values in the columns it self
        # skip if cell is 0
        # return the maxVal
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSquareLength = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue
                else:
                    above = matrix[row-1][col] if row > 0 else 0
                    left = matrix[row][col-1] if col > 0 else 0
                    upperLeft = matrix[row-1][col-1] if row > 0 and col > 0 else 0
                    matrix[row][col] = min(int(above), int(left), int(upperLeft)) + 1

                    if matrix[row][col] > maxSquareLength:
                        maxSquareLength = matrix[row][col]
        print(matrix)
        return maxSquareLength * maxSquareLength
                
        