class Solution:
    def trap(self, height) -> int:
        if len(height) < 3:
            return 0
        
        water = 0
        leftI = 0
        rightI = j = 2
        
        # go from back to front for less time
        while j <= len(height) - 1:
            if height[j] > height[rightI]:
                rightI = j
            j += 1
            
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            # if the current height > height[leftI]: leftI = i
            if height[i] >= height[leftI]:
                leftI = i
            # if i >= rightI, then find the next rightI
            if i == rightI:
                # findNextMaxOnRight
                j = rightI = i + 1
                while j <= len(height) - 1:
                    if height[j] > height[rightI]:
                        rightI = j
                    j += 1
            water += max(min(height[leftI], height[rightI]) - height[i], 0)             
        return water
## the above solution is still slower that the efficient solution, but I couldnt solve it

### too slow
#         # min(left, right) - height[i] <-- amount of water at index i
#         # maximum height on my left and maximum height on my right, min of that - height[i]
#         water = 0
#         left, right = 0, 0
        
#         for i in range(len(height)):
#             if i == 0 or i == len(height) - 1:
#                 continue
#             start, end = i - 1, i + 1
#             left = height[start]
#             right = height[end]
            
#             while start >= 0 or end <= len(height) - 1:
#                 if start >= 0 and height[start] > left:
#                     left = height[start]
#                 if end <= len(height) - 1 and height[end] > right:
#                     right = height[end]
#                 start -= 1
#                 end += 1
#             water += max(min(left, right) - height[i], 0)
            
#         return water