
"""
Given a string, determine if a permutation of the string could form a palindrome.
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # if there is no string, return False
        if len(s) == 0:
            return False
        
        # if the number of times each letter is repeated is even then True
        # if there is only one unique letter that's not reapeated then still True
        uniqueLetters = {}
        for character in s:
            if character in uniqueLetters:
                uniqueLetters.pop(character)
            else:
                uniqueLetters[character] = 1
        if len(uniqueLetters) > 1:
            return False
        return True