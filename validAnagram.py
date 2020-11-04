class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1

        for i in range(len(t)):
            if t[i] not in letters:
                return False
            if letters[t[i]] == 1:
                letters.pop(t[i])
            else:
                letters[t[i]] -= 1
        
        if len(letters) == 0:
            return True
        
        # obviously we could also do
        """ return sorted(s) == sorted(t) """
        # which is one line answer but it is O(N.logN)
        # The one above is a linear solution
        # depending on how large n could be you might want to use the lower one