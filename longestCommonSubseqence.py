class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        We will have to do a dynamic programming solution for this one
        
        Here's the idea:
        1. I thought about comparing from the start but it wont make sense that way, we need to go from the back to front
        2. Compare the letters at the end, if they match, add one to the answer, remove the letters and call the function again
        3. if the letters at the end do not match, branch out, send input1, input2 without last letter and vice versa calls
        4. pretty self explanatory after that
        
        """
        # base cases when we should return an integer
    
        
#         subsequenceCount = 0
#         if text1[-1] == text2[-1]:
#             subsequenceCount += 1
#             subsequenceCount += self.longestCommonSubsequence(text1[:len(text1)-1], text2[:len(text2)-1])
#         else:
#             subsequenceCount += max(self.longestCommonSubsequence(text1[:len(text1)-1], text2), self.longestCommonSubsequence(text1, text2[:len(text2)-1]))
#         return subsequenceCount

        # Alright so this is not very effective, because we are not using memoization
        # even with memoization, it is not ideal
        # we should make a DP table
        
#         [      " ""B""C
#             " "[x, x, x],
#             "B"[x, x, x],
#             "C"[x, x, x]
#         ]
        
#         this dynamic problem looks at prefixes: 
#             DP(i) = max(DP(x[:i], y[:i-1]), DP(x[:i-1], y[:i]), DP(x[:i-1], y[:i-1]) + 1 if matched)

        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        dpIndices = {}
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dpIndices[(i, j)] = 1 + dpIndices.get((i-1, j-1), 0)
                else:
                    dpIndices[(i, j)] = max(dpIndices.get((i,j-1), 0), dpIndices.get((i-1,j), 0))
                
        return dpIndices[len(text1)-1, len(text2)-1]
                    
                
                
                
                
                
                