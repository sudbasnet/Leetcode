import queue

"""
keep copying a letter at a time that is different from the endWord and check if it is in the 
wordList, if not, scrap it if it is then take it

number of letters is the number of branches at each point,
so for "hit" -> "cog"

"hit" transforms to "cit", "hot", "hig"
only "hot" exists in the dictionary, so apply the same logic to "hot" add the counter
return the min counter from each branch

code
----
counter = 0
def functionCall(counter, beginWord):
    for i in range(len(beginWord)):
        if beginWord[i] != endWord[i]:
            beginWord = beginWord[0:i] + endWord[i] + beginWord[i+1:]
            if beginWord in wordList:
                counter += 1
                return min(counter, functionCall(counter, beginWord))
            else:
                return float("inf")

"""
"""
the hint suggests that I need to rearrange the given data
so that I treat everything like a BFS

everything that satisfies a certain pattern is a level of BFS
"""
import queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seenWords = {beginWord: True}
        for word in wordList:
            seenWords[word] = False
            
        seenPatterns = []
        q = queue.Queue()
        q.put(beginWord)
        
        level = 1
        levelItems = 1
         
        while not q.empty():
            currentWord = q.get()
            for i in range(len(currentWord)):
                if currentWord[:i] + '*' + currentWord[i+1:] in seenPatterns:
                    continue
                for word in wordList:
                    if seenWords[word]:
                        continue
                    if word[:i] + word[i+1:] == currentWord[:i] + currentWord[i+1:]:
                        if word == endWord:
                            return level + 1
                        q.put(word)
                        seenWords[word] = True
                seenPatterns.append(currentWord[:i] + '*' + currentWord[i+1:])
                
            levelItems -= 1
            if levelItems == 0:
                levelItems = q.qsize()
                level += 1
                
        return 0
        # if m is len of beginWord
        # if n is num of words <- O(m * n^2)