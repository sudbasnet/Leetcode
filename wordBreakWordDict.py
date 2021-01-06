import collections 

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        think BFS
        the main word is the root node. 'catsandog', ['cat', 'cats', 'dog', 'sand', 'and', 'cat']
        the branches are: 'sandog' and 'andog'
        now keep repeating, and if see a node with no characters return True
        
        '''
        
        queue = collections.deque()
        self.words = collections.Counter(wordDict)
        self.seen = set()
        def getBranches(string):
            branches = []
            for i in range(len(string)):
                if string[:i+1] in self.words and string[i+1:] not in self.seen:
                    branches.append(string[i+1:])
                    self.seen.add(branches[-1])
            return branches
                    
        queue.append(s)
        while queue:
            current = queue.popleft()
            if not current:
                return True
            queue.extend(getBranches(current))
            
        return False