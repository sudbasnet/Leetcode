class Solution:
    def oddEvenJumps(self, A: [int]) -> int:
        if len(A) <= 1:
            return len(A)
        
        canJump = [{"even": False, "odd": False} for a in A]
        canJump[len(A) - 1] = {"even": True, "odd": True}
        goodJumps = 1
        
        def nextLargestIndexArray():
            stack = []
            nextLargestArray = [0 for a in A]
            # storing index and value, sorting by value
            sortedA = sorted([[a, i] for i, a in enumerate(A)])
            for [_, i] in sortedA:
                while stack and stack[-1] <= i:
                    nextLargestArray[stack.pop()] = i
                if not stack or stack[-1] > i:
                    stack.append(i)
            return nextLargestArray
                        
        def nextSmallestIndexArray():
            stack = []
            nextSmallestArray = [0 for a in A]
            # storing index and value, sorting by value
            sortedA = sorted([[-a, i] for i, a in enumerate(A)])
            for [_, i] in sortedA:
                while stack and stack[-1] <= i:
                    nextSmallestArray[stack.pop()] = i
                if not stack or stack[-1] > i:
                    stack.append(i)
            return nextSmallestArray
                
        nextLargestArray = nextLargestIndexArray()
        nextSmallestArray = nextSmallestIndexArray()

        for i in reversed(range(len(A) - 1)):
            nextLargest = nextLargestArray[i]
            nextSmallest = nextSmallestArray[i]
            if nextLargest > 0 and canJump[nextLargest]["even"]:
                goodJumps += 1
                canJump[i]["odd"] = True
            if nextSmallest > 0 and canJump[nextSmallest]["odd"]:
                canJump[i]["even"] = True
            
        return goodJumps
            