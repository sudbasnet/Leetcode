"""
Given a collection of distinct integers, return all possible permutations.
"""

def nextPermutations(listSoFar, remainingNumbers):
    allPermutations = []
    if len(remainingNumbers) <= 1:
        return [listSoFar + remainingNumbers]
    for i in range(len(remainingNumbers)):
        allPermutations += nextPermutations(listSoFar + [remainingNumbers[i]], remainingNumbers[:i] + remainingNumbers[i+1:])
    return allPermutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nextPermutations([], nums)

    
# O(n!)