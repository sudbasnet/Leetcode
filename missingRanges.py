"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

"""
class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        """
        list of integers  0 ... [4, 5, 7, 10]... 20
        lower and a upper bounds inclusive
        
        add immediately:
            add the first range 
            add the last range
        """
        if upper < lower:
            return []
        
        def makeString(start, end):
            if start == end:
                return str(start)
            return str(start) + "->" + str(end)
        
        if not nums:
            return [makeString(lower, upper)]
        
        ranges = []
            
        if nums[0] > lower:
            ranges.append(makeString(lower, nums[0] - 1))

        for i in range(len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                ranges.append(makeString(nums[i] + 1, nums[i + 1] - 1))
                
        if nums[-1] < upper:
            ranges.append(makeString(nums[-1] + 1, upper))
                           
        return ranges