       
class Solution:
    def makesSquare(self, words):
        diag = 0
        while diag < len(words):
            for i in range(diag, len(words)):
                if words[diag][i] != words[i][diag]:
                    return False
            diag += 1
        return True
    
    def wordSquares(self, words: [str]) -> [[str]]:
        # define the subroutine
        def getSquares(wordsSoFar):
            if len(wordsSoFar) == len(words[0]):
                return [wordsSoFar]
            squares = []
            for word in words:
                if self.makesSquare(wordsSoFar + [word]):
                    squares+= getSquares(wordsSoFar + [word])
            return squares
        
        return getSquares([])
        
    """
    one way I can see that we might be able to optimize is, go through the whole list and save 
    the starting letter of each word and save the list of words starting from that letter
    eg: if "lamb", "lamp", and "lame" are part of the list, we will have a dictionary that will save {"l": ["lamp", "lame", "lamb"], ...}
    so the next time, we are looking for a letter starting from l we only look here.
    """
        