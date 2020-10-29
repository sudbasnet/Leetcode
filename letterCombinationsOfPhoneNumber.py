ALPHABETS = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
    
def getWords(digitString, wordSoFar):
    options = ALPHABETS[digitString[0]]
    
    if len(digitString) == 1:
        return [wordSoFar + o for o in options]
    else:
        results = []
        for o in options:
            results += getWords(digitString[1:], wordSoFar + o)
        return results
        
# output  -> List[str]
class Solution:
    def letterCombinations(self, digits: str):
        """
        looks like a recursive problem, we need to explore each of the possibility
        of alphabets. If we see 2, we need to go to three branches, 'a', 'b' and 'c'.
        
        so lets look at how we can find out which letters are associated with which alphabets
        
        we could simply write it down in a dictionary
        """
        if digits == "":
            return []
        return getWords(digits, "")