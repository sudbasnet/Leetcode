'''
You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. 
pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], 
the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the 
index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).
'''
import random

class Solution:

    def __init__(self, w):
        # self.probabilities = self.getProbabilities(w)
        self.probs = self.getProbabilities(w)
    
    def getProbabilities(self, weights):
        totalSum = sum(weights)
        probs = []
        for i, wt in enumerate(weights):
                probs.append([wt/totalSum, i])
        probs.sort(reverse=True)
        
        prev = 0
        for i in range(len(probs)):
            probs[i][0] += prev
            prev = probs[i][0]

        return probs
        
    def pickIndex(self) -> int:
        randomValue = random.random()
        start, end = 0, len(self.probs) - 1
        while start <= end:
            mid = (start+end)//2
            if (mid == 0 or self.probs[mid-1][0] < randomValue) and randomValue <= self.probs[mid][0]:
                return self.probs[mid][1]
            if randomValue > self.probs[mid][0]:
                start = mid + 1
            else:
                end = mid - 1
        return 0

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()