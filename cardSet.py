"""
Card has 4 attributes (color, count, shading, shape), each attribute can have value 0, 1 or 2. 
3 cards are considered as a set if for each attribute, 3 cards either have the same value or have different value from each other. For example:
card1 (2, 0, 1, 2), card2 (1, 0, 0, 1) and card3(0, 0, 2, 0) are 1 set.
card1(2, 0, 1, 2), card2 (1, 1, 0, 1) and card3(0, 1, 2, 0) are not 1 set.

    write a boolean function with 3 cards as input. This function returns true if they are 1 set, otherwise returns false.
    Now given a collection of cards, return true if there is a set of cards exsits, otherwise return false. The interviewer wants O(n^2) solution.
"""

def isCardSet(card1, card2, card3):
    for i in range(4): # since 4 attributes
        currentSet = set()
        currentSet.add(card1[i])
        currentSet.add(card2[i])
        currentSet.add(card3[i])
        if len(currentSet) == 2:
            return False
    return True

# O(m * n) or O(n^2)
"""
Given an array i.e. [1, 2, 3, 5, 6, 7, 8] and a value k i.e. 3. If there is a subarray with length of 2k satisfies a sequence 
[a, a + 1, a + 2 ... a + k - 1, b, b + 1, b + 2... b + k - 1]. Return the beginning index of this subarray. So with given array 
[1, 2, 3, 5, 6, 7, 8] and k = 3, it can return 0 as [1, 2, 3, 5, 6, 7] satisfies the sequence requirement. If with given array 
[1, 3, 5, 6, 7, 8] and k = 3, it return -1 as there is no such subarray exsits.

k = 3
1, 2, 3, 4, 5, 7, 8, 10
"""
def subArrayIndex(arr, k):
    startIndex = 0
    for i in range(1, len(arr)):
        currentLen = i - startIndex
        if currentLen >= 2 * k:
            return startIndex

        if arr[i] -1 != arr[i-1]:
            if k <= currentLen < 2 * k:
                startIndex = i - k
            else:
                startIndex = i
    return -1

print(subArrayIndex([1, 2, 3, 5, 6, 7, 8], 4))