"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

 
 """
class Solution:
    def groupWords(self, word):
        letter = ''
        groups = []
        for i in range(len(word)):
            if word[i] == letter:
                groups[-1][1] += 1
            else:
                letter = word[i]
                groups.append([letter, 1])
        return groups
        
    def canExtend(self, groupedS, word):
        groupedWord = self.groupWords(word)
        if len(groupedS) != len(groupedWord):
            return False
        
        for i in range(len(groupedS)):
            if groupedS[i][0] != groupedWord[i][0]:
                return False
            if groupedS[i][1] != groupedWord[i][1] and (groupedWord[i][1] > groupedS[i][1] or groupedS[i][1] < 3):
                return False
            
        return True
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        """
        I will have to go linearly for each word
        if the stretchy word and the letter in the main word is the same,
        start a new group. save the group size so far, if you need to extend, 
        then make sure you extend so that the group size is atleast 3
        """
        result = 0
        groupedS = self.groupWords(S)
        for word in words:
            result += (1 if self.canExtend(groupedS, word) else 0)
        
        return result
                