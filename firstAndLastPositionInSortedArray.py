class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        """
        sorted => binary search
        
        linear 
        ------
        go through the list, when you see target: note the index
        when you stop seeing the target, note the last index
        return both indexes
        
        logN (binary search)
        do two binary searches???
        --------------------
        --------------------
        find the target but the target's left should be less than target or start of array
        find the target again but the target's right should be greater than target or end of arr
        
        CODE
        ----
        start, end = 0, len(arr) - 1
        
        mid = (start + end)//2
        
        if arr[mid] == target and arr[mid - 1] < target:
            found the first index
        if arr[mid] > target or (arr[mid] == target and arr[mid - 1] == target):
            go left
        if arr[mid] < target:
            go right
            
        pretty much the reverse of this for another index
        """
        def numsAt(index):
            if index < 0:
                return float("-inf")
            elif index >= len(nums):
                return float("inf")
            return nums[index]
        
        firstIndex, lastIndex = -1, -1
        
        # find firstIndex
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if numsAt(mid) == target and numsAt(mid - 1) < target:
                firstIndex = mid
                break
            elif numsAt(mid) < target:
                start = mid + 1
            else:
                end = mid - 1
                
        # find lastIndex
        start, end = 0, len(nums) - 1   
        while start <= end:
            mid = (start + end)//2
            if numsAt(mid) == target and numsAt(mid + 1) > target:
                lastIndex = mid
                break
            elif numsAt(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return [firstIndex, lastIndex]
        
        
        
        
        
        
        
        
        
        
        
        