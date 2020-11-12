class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        One of the solutions that I can think of is by considering multiple options
        but here, the branches could be too large. For example, I cant just consider 
        every possibility, that would be absurd.
        
        how about we sum up everything and save the running sum first
        [7,2,5,10,8]
        runningSums = [7, 9, 14, 24, 32]
        
        say we take 7 then remaining woul be 32 - 7 = 25
        say we take 9 so we got left 23
        say we take 14, so we got left with 18 ???
        
        not sure how to do it!!!
        
        might need to look at the hints
        """
        """
        one way would be to try every way the arrays could be split but that would be too time consuming
        
        after looking at the hints, i saw that we need to use binary search somehow
        so the idea has become, you find the max sum you can have, and the min sum you could have
        and basically do binary search to find the least point(maxsum) where the array can be broken into m pieces


        """
        # maximum the array could sum up to
        largestPossible = 0
        # the least value, max of the nums in the array
        lowestPossible = 0
        
        for i in range(len(nums)):
            lowestPossible = max(lowestPossible, nums[i])
            largestPossible += nums[i]
        
        while lowestPossible < largestPossible:
            mid = (largestPossible + lowestPossible)//2
            if self.splitIntoPieces(nums, mid) > m:
                lowestPossible = mid + 1
            else:
                '''there might be multiple ways to break the string into m parts 
                but with larger sums, so we still recurse and not return mid, 
                but instead we rescurse until we find the minimum sum one.'''
                largestPossible = mid
        return lowestPossible # or can return largestPossible, they are same at this point
            
    def splitIntoPieces(self, nums, maxSum):
        runningSum = 0
        numberOfSplits = 1 # least is one, what we got as input
        for i in range(len(nums)):
            if runningSum + nums[i] > maxSum:
                numberOfSplits += 1
                runningSum = nums[i]
            else:
                runningSum += nums[i]
        return numberOfSplits
                
        
        
        
                