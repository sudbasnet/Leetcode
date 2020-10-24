# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize 
the number of calls to the API.
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        is there always a bad version. 
        '''
        """
        logic
        -----
        start, end = 0, len(nums) - 1
        mid = (start + end) // 2
        if we get pushed out of the array, then there are no bad versions
        """
        
        def isBad(version):
            if version < 1 or version > n:
                return None
            return isBadVersion(version)
        
        start, end = 1, n
        
        while start <= end:
            mid = (start + end) // 2
            if isBad(mid) and isBad(mid - 1):
                end = mid - 1
            elif not isBad(mid):
                start = mid + 1 
            else:
                return mid
                
        return 0
        
        