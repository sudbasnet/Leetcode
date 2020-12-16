class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        After looking the examples:
        I can see that each element's position is a[i][j] so if I change that to a[j][i]
        then it is in the right position but on the wrong end
        so if I first switch a[i][j] with a[j][i] then flip the whole matrix horizontally
        then we can achieve the result we want
        
        Note: If I flip twice, then things will be exactly as we started. So we can only flip 
        two indices once.
        
        """
        if not matrix or not matrix[0]:
            return
    
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]
        