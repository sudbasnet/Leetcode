from heapq import heapify, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        # capture the number of times something occurs
        # hash table {letter: number of times it appeared}
        # turn that into a heap order by freq descending (make freq negative)
        # heappop and repeat based on the freq returned
        
        result = ""
        letters = {}
        
        for i in range(len(s)): # linear time, O(n)
            letters[s[i]] = letters.get(s[i], 0) + 1
        
        letterList = [[-val, key] for key, val in letters.items()]
        heapify(letterList) # linear time, in-place, O(n)
        
        while letterList: # O(n)
            [repeat, letter] = heappop(letterList) # O(log(n))
            result += letter * (-repeat)
        
        return result # O(n.log(n))