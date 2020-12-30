'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

    S will consist of lowercase letters and have length in range [1, 500].
'''


import collections
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        I tried dynamic programming, that was the wrong choice.
        
        Could just use heaps. Put the one with the highest freq and the second highest freq
        alternatingly.
        '''
        
        counts = collections.Counter(S)
        heap = []
        for k, v in counts.items():
            heap.append([-v, k])
        heapq.heapify(heap)

        prev = None
        result = []
        
        while len(result) < len(S):
            if not prev and heap:
                # if this is the first round, then just pop()
                prev = heapq.heappop(heap)
            elif heap:
                # fetch the top letter, then push the current prev
                prev = heapq.heapreplace(heap, prev)
            # if any letter is left (prev[0] < 0) then add it to result
            if prev[0] < 0:
                result.append(prev[1])
                # decrease the number of chars left
                prev[0] += 1

        # we can now check the last two elements, if they are same then return ""
        if len(result) >=2 and result[-1] == result[-2]: 
            return ""
        # return the things in the result array
        return ''.join(result)