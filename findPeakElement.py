class Solution:
    def findPeakElement(self, nums) -> int:
        """
        Its actually a pretty simple question, I am just a stupid person.
        so if a number on the right or left of any point goes up, it has to come down at some point
        and since no two numbers can be same that means the "slope" is always up or down
        and since the edges nums[-1] and nums[len(nums)] is considered -inf,
        there is always a peak somewhere. So just do a binary search, anf find that freaking peak
        """
        # there should be at least one element
        
        """
        logic:
        ------
        start, end, mid
        condition to move left: if nums[mid-1] > mid[mid}
        condition to move right: if nums[mid + 1] > mid[mid]
        mid is the result if nums[mid-1] < nums[mid] > nums[mid + 1] 
        """
        if len(nums) == 0:
            return -1
        
        def numsAt(i):
            if i == -1 or i == len(nums):
                return float('-inf')
            return nums[i]
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if numsAt(mid + 1) > numsAt(mid):
                start = mid + 1
            elif numsAt(mid - 1) > numsAt(mid):
                end = mid - 1
            else:
                return mid

            