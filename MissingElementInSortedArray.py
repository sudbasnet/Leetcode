'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

'''

class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        '''
        
        missingCounter = 0
        index = 0
        
        if current + 1 != next then update the current number
        if current + 1 == next then increase index
        '''
        # missingCounter, i = 0, 0
        # while missingCounter < k:
        #     if nums[i] + 1 == (nums[i+1] if i < len(nums)-1 else nums[i]):
        #         i += 1
        #     elif nums[i] + 1 != (nums[i+1] if i < len(nums)-1 else nums[i]):
        #         nums[i] += 1
        #         missingCounter += 1
        #     if missingCounter == k:
        #         return nums[i]
        
        '''
        first char, last char 10 - 4 + 1 = 7 digits. (lets say two nums are missing)
        if the len(nums) < 7: then 7 - len(nums) nums are missing
        
        '''
        missing = (nums[-1] - nums[0] + 1) - len(nums)
        
        if k > missing:
            return nums[-1] + (k - missing)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end)//2
            missing = (nums[mid] - nums[start] + 1) - (mid - start  + 1)
            if missing < k:
                start = mid
                k -= missing
            else:
                end = mid

        return nums[start] + k
