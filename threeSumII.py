""" Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
"""
"""
pretty sure this is not very efficient
"""
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        """
        this would still be n^2
        """
        nums.sort()
        
        difference = float('inf')
        bestSum = 0
        
        while nums:
            checkFor = nums.pop()
            newTarget = target - checkFor
            start, end = 0, len(nums)-1
            while start < end:
                currentDifference = abs(newTarget - nums[start] - nums[end])
                if currentDifference < difference:
                    bestSum = checkFor + nums[start] + nums[end]
                    difference = currentDifference
                if nums[start] + nums[end] > newTarget:
                    end -= 1
                else:
                    start += 1
        
        return bestSum
                
            