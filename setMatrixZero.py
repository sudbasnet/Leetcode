'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

'''

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        we will need to go through the whole matrix and update the first row,
        put a 0 if the column will contain zero in the final design. Do the same for 
        the cols, put a zero in the beginning of each row if is is going to be zero.
        also find out if this first row and first col will eventually be all zeros or not.
        if so, change this row and col last.
        
        """
        if not matrix or not matrix[0]:
            return
        
        firstRowIsZero, firstColIsZero = False, False
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c], matrix[r][0] = 0, 0
                    if r == 0: firstRowIsZero = True
                    if c == 0: firstColIsZero = True

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
            if firstColIsZero: matrix[r][0] = 0
        if firstRowIsZero: matrix[0] = [0 for _ in matrix[0]]


