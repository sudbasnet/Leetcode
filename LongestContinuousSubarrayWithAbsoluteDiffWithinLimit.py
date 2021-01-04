import collections


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """
        there should be two deques dqMin and dqMax

        smallest smaller small.....
        largest larger large .....

        if one of them fails, you move forward and go to the next largest that will be 
        within the range

        """
        if not nums:
            return 0

        dqMin, dqMax = collections.deque(), collections.deque()
        maxlen = 0
        start = 0
        for i in range(len(nums)):
            # remember dqMin should have elements:
            # smallest, smaller, small, less small, ...
            while dqMin and nums[dqMin[-1]] > nums[i]:
                dqMin.pop()
            dqMin.append(i)
            # remember dqMax should have elements:
            # largest, larger, large, less large, ....
            while dqMax and nums[dqMax[-1]] < nums[i]:
                dqMax.pop()
            dqMax.append(i)

            # if the max - min is not within limit, then move the start cursor
            while abs(nums[dqMax[0]] - nums[dqMin[0]]) > limit:
                # whatever the min of min and max indexes are, that +1 can be used as new start
                start = min(dqMax[0], dqMin[0]) + 1
                # clean up if the existing elements are outside of the window
                while dqMin and dqMin[0] < start:
                    dqMin.popleft()
                while dqMax and dqMax[0] < start:
                    dqMax.popleft()

            maxlen = max(maxlen, i - start + 1)

        return maxlen
