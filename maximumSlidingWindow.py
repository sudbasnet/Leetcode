import collections


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        '''
        need to create a deque (double-ended queue).

        '''
        if not nums or len(nums) < k:
            return []

        dq = collections.deque()
        result = []

        '''keep adding the indexes of the numbers in the dq
        as long as they are smaller than the tail of the dq
        
        obviously, remove the elements that are out of range (k)
        from the front of the deque, and remove anything that is 
        smaller than the current element from the end of the dq.
        '''
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])

        return result  # O(n+k)
