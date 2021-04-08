class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        at each point in the list, I am looking at how far can I reach,
        the max I can reach is the current value I am at. 
        So we check if the maxReach when checking at the last index is larger than
        the reach I have currently, then the maxReach remains the same.
        I can stop if the maxReach so far was the current index and the value at the
        current index is 0, ie: I cannot go forward
        """
        maxReach = 0
        for i in range(len(nums)):
            if i + nums[i] > maxReach:
                maxReach = i + nums[i]
            if maxReach >= len(nums) - 1:
                return True
            elif maxReach == i:
                return False
            
        