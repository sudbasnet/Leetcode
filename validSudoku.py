'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        can we find out what row we are on?? Yes
        can we find out what col we are on?? yes
        can we find out which square we are on?????? if row//3   0, 1 or 2 and col//3 0,1 or 2
            (0,0), (0,1) ... 
            
        make three dictionaries:
        rows = { 1:, 2: ... 9: }
        cols = { 1:, 2: ... 9: }
        squares = { ... 9}
        
        '''
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        squares = collections.defaultdict(list)
        
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                if val != '.':
                    rows[r].append(val)
                    cols[c].append(val)
                    squares[(r//3, c//3)].append(val)
        
        return True
                
                