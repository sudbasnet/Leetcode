class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        nope, so I completely misunderstood the problem
        we need to get the unique letters, thats simple enough
        but we also need to make sure that they are in the best lexicographical order possible
        while picking the objects in the string in order
        """
        """
        coding steps:
        -------------
        store locations in a dictionary
        go through the array again, add letter if it has not appeared yet
        add another letter, check if this letter is smaller than the last letter in the string
        if new letter is smaller that the last letter, see if theres another of the last letter in the string,
        if so remove the last letter else leave it and add the new one.
        """
        
        letterPositions = {}
        letterAdded = {}
        for i in range(len(s)):
            letterPositions[s[i]] = letterPositions.get(s[i], []) + [i]
            letterAdded[s[i]] = False
        
        result = ""
        for i in range(len(s)):
            if not letterAdded[s[i]]:
                while len(result) > 0 and (result[-1] > s[i] and letterPositions[result[-1]][-1] > i):
                    letterAdded[result[-1]] = False
                    result = result[:len(result) - 1]
                result += s[i]
                letterAdded[s[i]] = True
        
        return result;