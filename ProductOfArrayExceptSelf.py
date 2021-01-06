'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        just do left to right multiplications and store in one array
        then do right to left multiplications and store in another array
        
        then the product for index i is simply: products from leftToRight array before i
        multiplied to the products from rightToLeft after i
        '''
        result = [0 for _ in nums]

        for i in reversed(range(len(nums))):
            result[i] = (result[i+1] if i < len(nums)-1 else 1) * nums[i]
        
        runningProd = 1
        for i in range(len(nums)):
            result[i] = runningProd * (result[i+1] if i < len(nums)-1 else 1)
            runningProd *= nums[i]
        
        return result
    
#         leftToRight = [0 for _ in nums]
#         rightToLeft = [0 for _ in nums]
        
#         i = 0
#         while i < len(nums):
#             j = len(nums) - 1 - i
#             leftToRight[i] = (leftToRight[i-1] if i > 0 else 1) * nums[i]
#             rightToLeft[j] = (rightToLeft[j+1] if j < len(nums)-1 else 1) * nums[j]
#             i += 1
        
#         for i in range(len(nums)):
#             nums[i] = (leftToRight[i-1] if i > 0 else 1) * (rightToLeft[i+1] if i < len(nums)-1 else 1)
        
#         return nums