'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, 
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 '''
import collections

class Solution:
    def longestArithSeqLength(self, A: list[int]) -> int:
        '''
        Use dynamic programming.
        the complexity will be n^2 but I cant think of anything better.
        
        at each point, you ask a number to give you the length of the best subsequence with a diff value.
        
        so we need to get a difference of each number with each number that comes after it.
        '''
        
        self.nums = A
        self.seen = {}
        
        self.locs = collections.defaultdict(list)
        for i in range(len(self.nums)):
            self.locs[self.nums[i]].append(i)
            
        def getSubSequence(i, diff):
            if (i, diff) in self.seen:
                return self.seen[(i, diff)]
            
            if self.nums[i] - diff in self.locs:
                for j in self.locs[self.nums[i] - diff]:
                    if j > i:
                        subSeqLen = 1 + getSubSequence(j, diff)
                        self.seen[(i, diff)] = subSeqLen
                        return subSeqLen
            return 0
        
        maxlen = 2
        for i in range(len(self.nums) - 1):
            for j in range(i+1, len(self.nums)):
                diff = self.nums[i] - self.nums[j]
                maxlen = max(maxlen, 2 + getSubSequence(j, diff))
        
        return maxlen
                