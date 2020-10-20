"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        go from right to left
        if current > next(on the left):
            mark that next spot
            
        starting from current position, go right and find the smallest
        number that is greater than the marked number
        
        swap them
        
        sort everything from current and right
        
        if nothing is marked, just sort everything
        """
        def findIndexOfClosestGreatest(num, nums):
            diff, ind = nums[0] - num, 0
            for i in range(len(nums)):
                if nums[i] > num and nums[i] - num < diff:
                    diff = nums[i] - num
                    ind = i
            return ind + 1

        mark = -1
        rightInd = len(nums) - 1
        while rightInd > 0:
            if nums[rightInd] > nums[rightInd - 1]:
                mark = rightInd - 1
                nextInd = findIndexOfClosestGreatest(nums[mark], nums[mark + 1:])
                nums[mark], nums[mark + nextInd] = nums[mark + nextInd], nums[mark]
                break
            rightInd -= 1
        nums[mark + 1:] = sorted(nums[mark + 1:])

        # O(n logn)
        
        