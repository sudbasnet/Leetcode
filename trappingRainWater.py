class Solution:
    def trap(self, height: [int]) -> int:
        """
        have leftBracket and rightBracket,
        start at the position where height[i] > height[i+1]
        make that position both leftBracket and rightBracket, assign rightBracket the 
        max height on the right
        now move the left and sum all water based on the gap
        until you either the rightBracket or anything larger than leftBracket.
        if you reach rightBracket, reset leftBrackt to current location, and find next rightBracket
        if you reach anything larger than leftBracket, this becomes new leftBracket
        """
                
        # calculate the index with the largest height so far
        # idea is to know what my right-most limit is everytime i'm moving in the array
        
        largestRightHeights = [-1] * len(height)
        largestLeftHeights = [-1] * len(height)
        rightIndex = len(height) - 1
        leftIndex = 0
        # going from back to front, 
        for i in reversed(range(len(height))):
            largestRightHeights[i] = i if height[i] > height[rightIndex] else rightIndex
            rightIndex = largestRightHeights[i]
        # going from front to back, 
        for i in range(len(height)):
            largestLeftHeights[i] = i if height[i] > height[leftIndex] else leftIndex
            leftIndex = largestLeftHeights[i]     
            
        # now just traverse through the array and calculae the difference in heights
        position = 1
        totalWater = 0
        while position < len(height) - 1:
            rightBracket = largestRightHeights[position]
            leftBracket = largestLeftHeights[position]
            water = min(height[leftBracket], height[rightBracket]) - height[position]
            totalWater += max(water, 0)   
            position += 1
        
        return totalWater

            