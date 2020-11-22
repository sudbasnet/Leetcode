class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        # just find out what is the largest number in the array when squared,
        # then fill it from the end
        result = [0] * len(A)
        resIndex = len(A) - 1
        pointer1, pointer2 = 0, len(A) - 1
        
        while pointer1 <= pointer2:
            if abs(A[pointer2]) > abs(A[pointer1]):
                result[resIndex] = A[pointer2] * A[pointer2]
                pointer2 -= 1
            else:
                result[resIndex] = A[pointer1] * A[pointer1]
                pointer1 += 1
            resIndex -= 1
        
        return result
