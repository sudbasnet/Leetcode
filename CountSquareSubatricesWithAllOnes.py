'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
'''

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        '''
            [0, 1, 1, 1]
            [1, 1, 1, 1] 
            [0, 1, 1, 1]

            look to the right down and right-down diagonally. 
            if any of these indexes dont exist then 1, else min(right, down, right-down) + 1.

            Do this from the bottom right to the top, the total number is the answer

            [0, 3, 2, 1]
            [1, 2, 2, 1] 
            [0, 1, 1, 1]
            
            I dont need to do this from bottom right. 
            Its the same either way
        '''
        if not matrix or not matrix[0]:
            return 0
        
        squareMatrices = 0
        rows, cols = len(matrix), len(matrix[0])
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if matrix[r][c] == 1:
                    right = matrix[r][c+1] if c < cols - 1 else 0
                    down = matrix[r+1][c] if r < rows - 1 else 0
                    rightDown = matrix[r+1][c+1] if c < cols - 1 and r < rows - 1 else 0
                    matrix[r][c] = 1 + min(right, down, rightDown)
                    squareMatrices += matrix[r][c]

        return squareMatrices