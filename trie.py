def buildTrie(self, words):
    self.trie = {}
    for i in range(len(words)):
        # for every word, reset to root
        node = self.trie
        
        for char in words[i]:
            if char in node:
                node = node[char]
            else:
                newNode = {}
                newNode['#'] = []
                node[char] = newNode
                node = newNode
            node["#"].append(i)