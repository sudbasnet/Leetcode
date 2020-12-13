"""
Given a sorted n-size array, there are k elements have been changed i.e. [1, 3, 5, 6, 4, 2, 12] (it might be changed from [1, 3, 5, 6, 7, 8, 12] with k = 2). 
Important to know is that k is unknown and k is much smaller than n. The task is to re-sort the entire array.

[-100, 2, -50, -10, -1, 0, 3, 4]
[2, 1, 5, 6, 4, 7, 5, 8, 12]
[3, 4, 2]

if left is greater and right is greater, then pull the object out, and right is smaller than the left
if left is smaller and right is smaller, then also pull the object out, and right is smaller than the left

if I have the unsorted array, put that in a heap
then mergesort

scratch that!!

just check if the current element is larger than the next, if so put it in the mixed array, else put it in sorted array
"""

def reSortArray(mixedArr):
    unsorted = []
    sortedArr = []

    while len(mixedArr) > 1:
        if mixedArr[0] > mixedArr[1]:
            unsorted.append(mixedArr.pop(0))
        else:
            sortedArr.append(mixedArr.pop(0))
    print(f"sorted: {sortedArr}, unSorted: {unsorted}")
    unsorted.sort()
    result = []
    i, j = 0, 0

    while i < len(sortedArr) or j < len(unsorted):
        if i < len(sortedArr) and j < len(unsorted):
            if sortedArr[i] < unsorted[j]:
                result.append(sortedArr[i])
                i += 1
            else:
                result.append(unsorted[j])
                j += 1
        else:
            result += sortedArr[i:] + unsorted[j:]
            return result

    return result


print(reSortArray([2, 1, 6, 4, 7, 5, 8, 12]))