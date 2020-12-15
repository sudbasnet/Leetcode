'''
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, 
but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.
'''
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """
        just go ahead and remove the dashes, and count the length
        divide by K, and modulo by K. Result of modulo is the number of letters we have in the first group
        everything else has K elements and join by "-"
        """
        cleanS = S.replace("-", "").upper()
        first = len(cleanS)%K
        result = cleanS[:first]
        
        for i in range(first, len(cleanS)):
            if i > 0 and (i - first)%K == 0:
                result += "-"
            result += cleanS[i]
        
        return result
        
        