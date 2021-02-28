class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

    def findNextLetters(self, prefix):
        current = self.root
        for pre in prefix:
            if pre not in current:
                return []
            current = current[pre]
        return list(current.keys())


class Solution:
    def findWords(self, board, words):
        '''
        creating a TRIE like datastructure is a smart choice here
        '''
        trie = Trie()
        for word in words:
            trie.insert(word)

        output = []
        # create a method to traverse through the board

        def traverse(prefix, point, visited):
            r, c = point
            if r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1:
                return
            prefix += board[r][c]
            if prefix in words:
                output.append(prefix)

            nextLetters = trie.findNextLetters(prefix)
