class Solution:
    def maxSubArray(self, nums) -> int:
        # Input: array of integers positive or negative or 0, could be repeated
        # Output: contigous subarray with the largest sum
        
        """
        how about we look at the sum so far, as we go from left to right,
        remember we need to return the sum not the array itself.
        
        Out main challenge here is to know when to ignore the elements that
        come before me??
        So, if (whatever comes before me) + (me) < (me), what's the point of 
        including anything before me, right?
        
        Code
        ----
        bestSum = float("-inf")
        runningSum = 0
        
        for loop:
            if me + runningSum < me:
                runningSum = me
        
        """
        
        bestSum = float("-inf")
        runningSum = 0
        
        for i in range(len(nums)):
            if runningSum + nums[i] < nums[i]:
                runningSum = nums[i]
            else:
                runningSum += nums[i]
            bestSum = max(bestSum, runningSum)
        
        return bestSum