import collections

## Solution 1: saving all the prefixes
## faster but uses alot of memory
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        Obviously it is a recursion..
        
        start with a word, put it in a list,...
        if the len of the list is k look at col k (ie: k+1th col)
        and find words starting with the elements of the kth col.
        
        to find the words starting with something, a trie datastructure 
        would be the best choice
        '''
        self.prefixes = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)-1):
                self.prefixes[word[:i+1]].append(word)
                
        self.boxes = []
        
        def nextMatch(box, words):
            if not box or not words:
                return
            if len(box) == len(words[0]):
                self.boxes.append(box)
                return
            # get the prefix
            col = len(box)
            prefix = ''
            for i in range(len(box)):
                prefix += box[i][col]
            # recursively call itself
            for matched in self.prefixes[prefix]:
                nextMatch(box + [matched], words)
                
        for word in words:
            nextMatch([word], words)
        
        return self.boxes

############## Solution using a Trie ###############
# slower but the memory usage is better 

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.word = word

    def wordsStartingWith(self, prefix):
        matchedWords = []
        current = self.root
        for pre in prefix:
            current = current.children.get(pre)
            if not current:
                return []
        # the obj current now contains all the words
        stack = [current]
        while stack:
            current = stack.pop()
            if current.word:
                matchedWords.append(current.word)
            for node in current.children.values():
                stack.append(node)
        return matchedWords
        
class Solution2:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        Obviously it is a recursion..
        
        start with a word, put it in a list,...
        if the len of the list is k look at col k (ie: k+1th col)
        and find words starting with the elements of the kth col.
        
        to find the words starting with something, a trie datastructure 
        would be the best choice
        '''
        self.trie = Trie()
        self.boxes = []
        
        for word in words:
            self.trie.insert(word)

        def checkWords(box):
            # if it is a square add to list
            if len(box) == len(box[0]):
                self.boxes.append(box)
                return
            # make the prefix
            prefix = ''
            for i in range(len(box)):
                prefix += box[i][len(box)]
            # recurse
            for matched in self.trie.wordsStartingWith(prefix):
                checkWords(box + [matched])
            
        for word in words:
            checkWords([word])
        return self.boxes 
