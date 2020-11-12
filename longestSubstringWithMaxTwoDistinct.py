"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        
        "cacabbaall"
        solution: "abba"
        
        firstLetter, secondLetter = "", ""
        
        longestString = 0
        firstLetterEnd <- first letter I see, index of last time i see it
        secondLetterEnd <- second letter I see, index of last time I see it
        
        lets say I see another letter we need to break at the point firstLetterEnd,
        new string starts at firstLetterEnd + 1
        
        before breaking, we check if the string so far is of length > longestString,
        if so, update longestString
        
        firstletterEnd = secondLetterEnd 
        and secondLetterEnd = new letter's index
        
        also check edge cases at the end
        also check if there's only the firstLetter, then return length of what we have so far.
        
        do a for loop
        and once we are done with the for loop, check if what we have at the end is longer than 
        longestString.
        """
        largestStringLength = 0
        firstLetter, secondLetter = "", ""
        firstLetterEnd, secondLetterEnd = -1, -1
        stringSoFar = ""
        
        if len(s) <= 2:
            return len(s)
        iteration = 0
        for i in range(len(s)):
            iteration += 1
            if firstLetter == "" and s[i] != secondLetter:
                firstLetter = s[i]
                firstLetterEnd = i
                stringSoFar += s[i]
                
            elif s[i] != firstLetter and secondLetter == "":
                secondLetter = s[i]
                secondLetterEnd = i
                stringSoFar += s[i]
            
            else: # we are in the middle somewhere
                if s[i] != firstLetter and s[i] != secondLetter:
                    # means we are going to make new string
                    largestStringLength = max(largestStringLength, len(stringSoFar))
                    # check what the last letter was
                    if stringSoFar[-1] == firstLetter:
                        stringSoFar = s[secondLetterEnd + 1: i+1]
                        secondLetter = s[i]
                        secondLetterEnd = i
                    else:
                        stringSoFar = s[firstLetterEnd + 1: i+1]
                        firstLetter = s[i]
                        firstLetterEnd = i
                else:
                    if s[i] == firstLetter:
                        firstLetterEnd = i
                    else:
                        secondLetterEnd = i
                        
                    stringSoFar += s[i]

        return max(largestStringLength, len(stringSoFar))
                    
                
        
        