class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        keep track of the indices that have the elements we are looking for
        [i1, i2, i3 ....]
        """
#         minimumString = ""
        
#         repeatsRequired = {}
#         occurances = {}
#         for j in range(len(t)):
#             if t[j] in repeatsRequired:
#                 repeatsRequired[t[j]] += 1
#             else:
#                 repeatsRequired[t[j]] = 1
#                 occurances[t[j]] = []
            
#         indices = []
        
#         for i in range(len(s)):
            
#             if s[i] in repeatsRequired and repeatsRequired[s[i]] >= 1:
#                 occurances[s[i]].append(i)
#                 repeatsRequired[s[i]] -= 1
#                 indices.append(i)
                
#             elif s[i] in repeatsRequired and repeatsRequired[s[i]] == 0:
#                 if occurances[s[i]][0] == indices[0]:
#                     indices.pop(0)
#                     occurances[s[i]].pop(0)
#                 else:
#                     indices.remove(occurances[s[i]][0])
#                     occurances[s[i]].pop(0)
#                 indices.append(i)
#                 occurances[s[i]].append(i)

#             if len(indices) == len(t):
#                 if minimumString == "" or (indices[-1] - indices[0] + 1) < len(minimumString):
#                     minimumString = s[indices[0]: indices[-1]+1]
                    
#                 occurances[ s[indices[0]] ].pop(0)
#                 repeatsRequired[s[indices[0]]] += 1
#                 indices.pop(0)
                
#         return minimumString
    
        '''
        WHat i came out with was a little complex but it was right.
        The easier way of doing it would be to simply have two pointers
        The second one moves as long as it does not satisfy the requirements.
        Once window satisfies, we record the string, then we move the first pointer
        as long as the string still satisfies and record the length.
        The moment it again does not qualify, we move the right pointer
        
        The following is much better
        '''
        minimumString = ""
        requiredRepeats = {}

        for letter in t:
            requiredRepeats[letter] = requiredRepeats.get(letter, 0) + 1
        
        left, right = 0, 0 
        found = 0
        while found < len(t) and left <= right and right < len(s) :
            
            if s[right] in requiredRepeats:
                if requiredRepeats[s[right]] > 0:
                    found += 1
                requiredRepeats[s[right]] -= 1

            while found == len(t) and left <= right:
                if minimumString == "" or len(minimumString) > (right - left + 1):
                    minimumString = s[left: right + 1]
                    
                if s[left] in requiredRepeats:
                    requiredRepeats[s[left]] += 1
                    if requiredRepeats[s[left]] > 0:
                        found -= 1
                left += 1
                
            right += 1
            
        return minimumString
            
                