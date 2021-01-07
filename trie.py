import collections
'''
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.word = word

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        if current.word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for pre in prefix:
            current = current.children.get(pre)
            if not current:
                return False
        return True

    def allWordsStartingWith(self, prefix: str) -> [str]:
        matchedWords = []
        current = self.root
        for pre in prefix:
            current = current.children.get(pre)
            if not current:
                return []
        # current trie at this point has all the words
        stack = [current]
        while stack:
            current = stack.pop()
            if current.word:
                matchedWords.append(val.word)
            for val in current.children.values():
                stack.append(val)
        return matchedWords

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('car')
obj.insert('card')
obj.insert('con')
obj.insert('apple')
print(obj.search('appe'))
print(obj.allWordsStartingWith('c'))
# param_3 = obj.startsWith(prefix)
'''
## second trie 

class Trie:
    def __init__(self):
        self.node = {}
    
    def insert(self, word):
        current = self.node
        for letter in word:
            if letter not in current: current[letter] = {}
            current = current[letter]
        current["word"] = word

    def search(self, word):
        current = self.node
        for letter in word:
            if letter in current: current = current[letter]
            else: return False
        if word in current: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.node
        for pre in prefix:
            if pre in current: current = current[pre]
            else: return False
        return True

    def wordsStartingWith(self, prefix: str) -> list[str]:
        matchedWords = []
        current = self.node
        for pre in prefix:
            if pre in current: current = current[pre]
            else: return []
        # current trie at this point has all the words
        stack = [current]
        while stack:
            current = stack.pop()
            if 'word' in current: 
                matchedWords.append(current['word'])
            for key, val in current.items():
                # add all except for the one with the 'word' key
                if key != 'word': stack.append(val)
        return matchedWords

obj = Trie()
obj.insert('car')
obj.insert('card')
obj.insert('con')
obj.insert('apple')
print(obj.search('appe'))
print(obj.wordsStartingWith('c'))
# print(obj.node)