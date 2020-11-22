"""
given a matrix, find max sum of any rectangle in it.
"""
def kanadeAlgo(arr):
    maxSum = float("-inf")
    runningSum = 0
    for i in range(len(arr)):
        if runningSum + arr[i] <= arr[i]:
            runningSum = arr[i]
        else:
            runningSum += arr[i]

        if runningSum > maxSum:
            maxSum = runningSum * 1
    return maxSum


def maxSumRectangleInMatrix(matrix: [[int]]):
    maxSum = float("-inf")
    # O(n^2)
    for left in range(len(matrix[0])):
        for right in range(left, len(matrix[0])):
            # O(n)
            newArr = [sum(matrix[row][left:right + 1]) for row in range(len(matrix))]
            newArrSum = kanadeAlgo(newArr)
            maxSum = max(maxSum, newArrSum)
    return maxSum
            
test = [
    [6, -5, -7, 4, -4],
    [-9, 3, -6, 5, 2],
    [-10, 4, 7, -6, 3],
    [-8, 9, -3, 3, -7]
]

print(maxSumRectangleInMatrix(test))
