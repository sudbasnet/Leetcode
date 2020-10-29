def addParanthesis(currentString, remainingLeft, remainingRight):
    # if no more left or right paranthesis left, return currentString
    if remainingLeft == 0 and remainingRight == 0:
        return [currentString]
    
    # cannot put a close paran without a open paren, so remainingRight needs to be nore
    elif remainingLeft > 0 and remainingRight > remainingLeft:
        return addParanthesis((currentString + "("), remainingLeft - 1, remainingRight) + addParanthesis((currentString + ")"), remainingLeft, remainingRight - 1)
    
    # if all done with left, only right remains
    elif remainingLeft == 0 and remainingRight > 0:
        return addParanthesis((currentString + ")"), remainingLeft, remainingRight - 1)
    
    # if equal left and right remains but not 0, can only put the left one
    elif remainingLeft > 0 and remainingLeft == remainingRight:
        return addParanthesis((currentString + "("), remainingLeft - 1, remainingRight)
    
    # if all else fails, return an empty array
    else:
        return []

class Solution: 
    """
    we need to use dynamic programming in this problem
    I tried to see the pattern in this problem by looking at a few examples
    but it was impossible to see every single pattern that could occur

    So, here's what we want to do:
    we keep track of how many left paranthesis we have left to open
    and how many right paranthesis we have left to close

    if we have more than 0 left paranthesis left, we open a left paranthesis and recurse.
    if we have more than 0 right paranthesis left and number of left parans left is 
    less than the number of right paranthesis left then add aright paranthesis and recurse.
    """
    def generateParenthesis(self, n: int): 
        return addParanthesis("(", n-1, n)
        
    
    