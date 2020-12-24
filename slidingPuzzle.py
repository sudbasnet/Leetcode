'''
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
'''
import queue

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        '''
        alright!!!!
        
        think BFS!!!
        keep transforming, if what I transform to already exists then leave it do others
        '''
        self.winningBoard = [1, 2, 3, 4, 5, 0]
        self.moves = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5}, 5:{2, 4}}
        
        board = board[0] + board[1]
        seenBoards = [board]
        
        q = queue.Queue()
        q.put(board)
        level = 0
        counter = 1
        
        while not q.empty():
            currentBoard = q.get()
            if currentBoard == self.winningBoard:
                return level
            
            zeroAt = currentBoard.index(0)
            for move in self.moves[zeroAt]:
                newBoard = currentBoard + []
                newBoard[move], newBoard[zeroAt] = newBoard[zeroAt], newBoard[move]
                if newBoard not in seenBoards:
                    seenBoards.append(newBoard)
                    q.put(newBoard)
                    
            if counter == 1: 
                level += 1
                counter = q.qsize()
            else:
                counter -= 1
                
        return -1