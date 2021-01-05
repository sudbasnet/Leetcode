'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists 
a sequence of moves to transform one string to the other.

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "X", end = "L"
Output: false

Example 3:

Input: start = "LLR", end = "RRL"
Output: false

Example 4:

Input: start = "XL", end = "LX"
Output: true

Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false

'''

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        looks like a tree
        
                   RXXL
        
           XRXL            XRLX 
        
        XXRL  XRLX     ....     ....
        
        Thinking of BFS
        obviously you could do BFS from both sides and which ever gives you the answer first, you return it.
        
        But this algorithm seems awefully slow for an input of size up to 10000
        '''
#         self.seen = set(start)
#         def moves(string):
#             strings = []
#             for i in range(len(string) -1 ):
#                 if string[i:i+2] == 'XL':
#                     newStr = string[:i] + 'LX' + string[i+2:]
#                     if newStr not in self.seen: strings.append(newStr)
#                 elif string[i:i+2] == 'RX':
#                     newStr = string[:i] + 'XR' + string[i+2:]
#                     if newStr not in self.seen: strings.append(newStr)
#             return strings
    
#         q = collections.deque()
#         q.append(start)

#         while q:
#             current = q.popleft()
#             if current == end:
#                 return True
#             for m in moves(current):
#                 if m not in self.seen:
#                     self.seen.add(m)
#                     q.append(m)
#         return False
        '''
        look at the problem properly, L and R both move left and right when they have 'X'
        next to them. But L and R cannot move accross each other. So that means, if we simply
        remove all occurances of 'X' from the string then the LLs and the RRs should be same 
        in the end and the start.
        
        remember that L can only move to left 
        and R can only move to right
        
        so the relative position of the Ls and Rs in the start should be such that
        the first L in the start should either be at the same index as the first 'L' in the end
        or it should be before the index of first 'L' in the end.
        
        similarly for 'R'.
        
        '''
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        startL = [i for i in range(len(start)) if start[i] == 'L']
        endL = [i for i in range(len(end)) if end[i] == 'L']
        for i, j in zip(startL, endL):
            if i < j: return False
        
        startR = [i for i in range(len(start)) if start[i] == 'R']
        endR = [i for i in range(len(end)) if end[i] == 'R']
        for i, j in zip(startR, endR):
            if i > j: return False
        
        return True
        
                
        