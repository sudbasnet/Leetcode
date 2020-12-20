import collections

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