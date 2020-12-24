import queue
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:

        q = queue.Queue()
        q.put(beginWord)

        level = 1
        levelItems = 1

        seenWords = {beginWord: True}
        patterns = collections.defaultdict(list)
        for word in wordList:
            seenWords[word] = False
            for i in range(len(word)):
                patterns[word[:i]+'*'+word[i+1:]].append(word)

        while not q.empty():
            currentWord = q.get()
            for i in range(len(currentWord)):
                if currentWord[:i]+'*'+currentWord[i+1:] not in patterns:
                    continue
                for word in patterns[currentWord[:i]+'*'+currentWord[i+1:]]:
                    if seenWords[word]:
                        continue
                    if word[:i] + word[i+1:] == currentWord[:i] + currentWord[i+1:]:
                        if word == endWord:
                            return level + 1
                        q.put(word)
                        seenWords[word] = True
                patterns.pop(currentWord[:i] + '*' + currentWord[i+1:])

            levelItems -= 1
            if levelItems == 0:
                levelItems = q.qsize()
                level += 1

        return 0
        # if m is len of beginWord
        # if n is num of words <- O(m * n^2)
