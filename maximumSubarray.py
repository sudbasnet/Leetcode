class Solution:
    def maxSubArray(self, nums) -> int:
        # so we use concept of dynamic programming.
        # we check at every element, if I add myself the sum so far, 
        # do I increase or decrease the sum??? if I increase the sum,
        # else I check if the sum by adding me is greater than myself.
        # if sumSoFar + nums[i] > nums[i], keep me, 
        sumSoFar = 0
        bestSum = float('-inf')
        
        for i in range(len(nums)):
            if sumSoFar + nums[i] > nums[i]:
                sumSoFar += nums[i]
            else:
                sumSoFar = nums[i]
                
            if sumSoFar > bestSum:
                bestSum = sumSoFar
                
        return bestSum
        # now find indexes that give the best difference
        
            
            