'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        
        
        [1, 0, 0, 0, 1, 0, 1, 1, 1]
        
        so we could calculate the distance to the last 1 on the right,
        and we could calculate the distant of the last 1 on the left.
        then we take the min of those two for each 0.
        we return the index with 0 with the max out of the min values
        '''
#         if len(seats) <= 1:
#             return 0

#         maxDist, left, right = 0, float('-inf'), 0
        
#         for i in range(len(seats)):
#             if seats[i] == 1:
#                 left = i
#             else:
#                 if right <= i:
#                     right = i
#                     while right < len(seats) and seats[right] == 0 : 
#                         right += 1
#                     if right >= len(seats): right = float('inf')
#                 maxDist = max(maxDist, min(i - left, right - i))
                
#         return maxDist
        '''
        checking out the solution made me realize I'm just stupid
        
        keep two pointers, last and current. last points to nothing in the beginning.
        once we find our first 1 we check if 'last' has a value, if not then current maxDist is the current index.
        If 'last' has a value then the current maxDist is (current - last)//2
        similarly if current is at the end but there is no 1, maxDist is last - current
        '''

        last, maxDist = None, 0
        for i, seat in enumerate(seats):
            if seat:
                if last is not None:
                    maxDist = max(maxDist, (i - last) // 2)
                else:
                    maxDist = max(maxDist, i)
                last = i
        if not seat:
            maxDist = max(maxDist, i - last)
        
        return maxDist
                    
