class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        """
        ok, so my solution was you do a binary search on every column 
        whose min and max had the fllowing rel with the target: min < target < max
        so that would be O(nlog(n))
        
        better solution is by space reduction
        you start at a corner either (lower left) or (upper right)
        upper right:
        if target is less you go left(col - 1) if target is more you go down (row - 1)
        keep going and when you find your target, you return True
        
        
        At least on LeetCode, my first technique is better
        """
        if not matrix or not matrix[0]:
            return False

        # first technique o[n.log(n)]
        # faster than 98.25 %, memory less than 8.95%
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                start, end = 0, len(matrix[i]) - 1
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        end = mid - 1
                    else:
                        start = mid + 1
        return False

#         # second technique
#         # faster than 61.32%, memory 39.01% better
#         # start a top right corner
#         seenRows = {}
#         seenCols = {}
#         row, col = 0, len(matrix[0]) - 1
#         while len(seenRows) < len(matrix) and len(seenCols) < len(matrix[0]):
#             if matrix[row][col] == target:
#                 return True
#             elif target < matrix[row][col]:
#                 seenCols[col] = True
#                 col -= 1
#             else:
#                 seenRows[row] = True
#                 row += 1
#         return False
        
        