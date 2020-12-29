class Solution:
    def solveNQueens(self, n: int):
        '''
        If I place a queen in a cell (r, c), then I cannot put another queen in row r or col c.
        additionally, I cannot put another queen where if (r + x, c + x) = (R, C),  r - R != c - C.
        
        
        valid next moves = nothing in the same r, nothing in the same c, and nothing where r - R == c - C
        '''
        self.n = n
        self.results = []
        
#         def nextMove(invalidSums, invalidDiffs, invalidRows, invalidCols):
#             for i in range(self.n):
#                 for j in range(self.n):
#                     if i not in invalidRows and j not in invalidCols and i+j not in invalidSums and i-j not in invalidDiffs:
#                         return (i,j)

                    
#         def putQueens(point):
#             r, c = point
#             invalidRows = {}
#             invalidCols = {}
#             invalidSums = {}
#             invalidDiffs = {}
#             stack = [point]
#             while stack:
#                 if len(stack) == self.n:
#                     self.results.append(stack)
#                     break
#                 current = stack[-1]
#                 invalidSums.add(current[0] + current[1])
#                 invalidDiffs.add(current[0] - current[1])
#                 invalidRows.add(current[0])
#                 invalidCols.add(current[1])
#                 move = nextMove(invalidSums, invalidDiffs, invalidRows, invalidCols)
#                 if move: stack.append(move)
#                 else: stack.pop()
        
#         for r in range(self.n):
#             for c in range(self.n):
#                 putQueens((r, c))
                
#         return self.results
        '''think I did pretty bad'''
        '''while the solution was mostly right, heres how I could have made it faster'''
        '''diagonals have r-R == c-C => r-c == R-C also r-c == -(R-C), so we could just save 
        the sums and the diffs and we can find out which cells are invalid'''
        def dfs(queens, diffs, sums):
            row = len(queens)
            if row == self.n:
                self.results.append(queens)
                return
            for col in range(self.n):
                if col not in queens and row-col not in diffs and row+col not in sums:
                    dfs(queens + [col], diffs + [row-col], sums + [row+col])
        
        dfs([], [], [])
        finalResults = []
        for result in self.results:
            finalResults.append(['.'*i + 'Q' + '.'*(self.n-i-1) for i in result])

        return finalResults
                
            
        