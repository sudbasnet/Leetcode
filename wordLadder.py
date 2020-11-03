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
def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    if endWord not in wordList:
        return 0
    
    # returns all the words matching a pattern except if it is in
    # the doNotIncludeList
    def getWordsWithPattern(pattern, wordList, doNotIncludeList):
        # the pattern would be of the form "*ot"
        # we return anything like "hot" "not" "lot" "got"
        matchedListOfWords = []
        for word in wordList:
            wordIsValid = True
            for i in range(len(word)):
                if word[i] != pattern[i] and pattern[i] != "*":
                    wordIsValid = False
            if wordIsValid and word not in doNotIncludeList:
                matchedListOfWords.append(word)
        return matchedListOfWords

    level = 1
    q = queue.Queue()
    q.put(beginWord)
    q.put("#")

    # we are adding a "#" to tell when a new level is reached
    # since we will always have a "#", the size will be 1 at least
    while q.qsize() > 1:
        currentWord = q.get()
        # just marking when we have reached another level
        if currentWord == "#":
            level += 1
            currentWord = q.get()
            q.put("#")

        for i in range(len(currentWord)):
            pattern = currentWord[:i] + "*" + currentWord[i+1:]
            matchedWords = getWordsWithPattern(pattern, wordList, [currentWord])
            if endWord in matchedWords:
                return level + 1
            for matchedWord in matchedWords:
                wordList.remove(matchedWord)
                q.put(matchedWord)
    return 0
        
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))