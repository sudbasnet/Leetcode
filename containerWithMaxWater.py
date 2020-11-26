class Solution:
    def maxArea(self, height: [int]) -> int:
        """
        Since we are looking for a range, we know it is a two pointer problem
        if we start with start and end pointers next to each other as we move forward, we will forget about the old values
        
        so we should start with the pointers at the very ends, since we just need to save max
        initialize a val, every time we move the indices we check the max
        the only logical way to move is that the pointer at the smaller height moves closer
        
        
        height: 2 3 5 2 3 5 8
        index:  0 1 2 3 4 5 6
        ans: 20
        """
        area = 0
        start, end = 0, len(height) - 1
        
        while start < end:
            currArea = (height[start] if height[start] < height[end] else height[end]) * (end - start)
            area = area if area > currArea else currArea
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return area
            
        
        
        
        