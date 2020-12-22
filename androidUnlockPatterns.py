class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """
        there will be a for loop starting from each point
        minimum of m points and maximum of n points
        """
        invalids = {(1,3): 2, (3,9): 6, (7,9): 8, (1,7): 4, (1,9): 5, (3,7): 5, (2,8): 5, (4,6): 5}
        
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.patternCount = 0
        self.m = m
        self.n = n
        
        def getNeighbors(num, visited):
            neighbors = []
            for i in self.board:
                invalidJump = (i,num) if i<num else (num,i)
                if invalidJump in invalids and invalids[invalidJump] not in visited:
                    continue
                if i not in visited:
                    neighbors.append(i)
            return neighbors
        
        def checkPattern(pathSoFar):
            if self.m <= len(pathSoFar) <= self.n:
                self.patternCount += 1
            if len(pathSoFar) < n:
                neighbors = getNeighbors(pathSoFar[-1], pathSoFar)
                for neighbor in neighbors:
                    checkPattern(pathSoFar + [neighbor])
            
        for i in self.board:
            checkPattern([i])
            
        return self.patternCount
        