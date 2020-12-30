class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        I couldn't really solve this one. So I had to get some help on youtube.
        
        The idea is:
        if the buildings keep increasing then we keep storing them in a stack. If we see
        something that is less than the last building we saw, then we pop the last building out 
        until we see something that is less than what we have right now. 
        
        so if we have buildings like this:
        
        2 3 4 5 6 ...... 
        
        we could potentially have a rectangle that is all 2s -----> till the end
        or we could potentially have a rectangle that is all 3s ----> till the end
        or we could potentially have a rectangle that is all 4 or 5 or 6 -----> till the end
        
        Its only when we see something smaller than those numbers that we know, the rectangle will
        not go further than the current point.
        
        so we calculate the rectangle we have so far. 
        
        so lets say the next element we see in the above array is 3 (2 3 4 5 6 3 ...... )
        when we are at the 3, (index = 5), we need to calculate what the previous buildings that are higher than 3
        have contributed so far. 
        6 has contributed 1 rectangle of size 6 that starts at index 4. 
        6 * ((i-1) - 3) here we can see i-1 is the right bound of the rectangle 6 and then the left bound is 3. 
        so the total area is 6 * ((5-1) - 3) = 6
        
        if we apply the same logic to the next highest which is 5 then we get
        5 * ((5-1) - 2) = 10 notice that this includes the sub-rectangle of size 5 at index 5 (val = 6))
        ...
        
        
        '''
        if not heights:
            return 0
        
        heights.append(0) # we add this so that we look at all the possible buldings
        maxArea = 0
        stack = [-1] # we do this because if there is nothing in the stack where we are storing heights, then left bound does not exist
        
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                maxArea = max(maxArea, heights[stack.pop()] * (i-1 - stack[-1]))
            stack.append(i)
        
        return maxArea
        