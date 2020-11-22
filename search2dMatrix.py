from math import ceil
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        since it is sorted, how about we do, binary search
        if we do two binary searches, first to find which row the value belongs in
        and then which col of the row the value belongs in, we should be good eh!
        """
        """
        Coding Steps:
        -------------
        for each row, we know the min and max element so we can see if min is greater than target
        then left portion
        if max of a row is less than the target, we go right portion, else we found the row
        """
        """
        OR!!!
        you could assume that the matrix is 1D and find a way to represent each row col combo with a single num
        
        so lets say
        [1, 2, 3, 4, 5]
        [6, 7, 8, 9, 10]
        [11, 12, 13, 14, 15]
        
        total values = 5 x 3 = 15
        the 12th value is 12%5 = 2th col,  12/5 = 2.5 ceil = 3rd row
        
        [1, 2]
        [3, 4]
        [5, 6]
        [7, 8]
        [9, 10]
        
        what is the 6th value??
        since we wrap around 2
        6/2 = 3rd row
        6%2 = 0 means end of row
        
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        
        nrows, ncols = len(matrix), len(matrix[0])
        
        def valueAt(rowCol):
            row = ceil(rowCol/ncols) - 1
            col = (rowCol%ncols) - 1
            print(f"value at {rowCol}: {matrix[row][col]}")
            return matrix[row][col]
            
        start = 1
        end = nrows * ncols 
        while start <= end:
            mid = (start + end) // 2
            if valueAt(mid) == target:
                return True
            if valueAt(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return False