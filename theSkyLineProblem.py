import heapq

class Solution:
    def getSkyline(self, buildings):
        """
        maybe I need to order this such that the leftmost point is the first element of 
        the sorted list.
        if the next element breaks/overlapps and has a height greater than the last element
        then startpoint of tall, height of small unless the taller building totally overlaps.
        If completely overlaps than height of taller.
        
        or just soft by leftPoint asc, then height desc
        
        so, i looked at the hints and turns out what I wanted to do was partially correct
        I need to find each point in the x axis and its corresponding height, I also need to 
        check if the point I am at is the starting point or ending point of a building.
        If a point is a start point, we will enter it into a heap, if its a leaving point, then
        we remove that point from the heap. If by removing the point or by entering a point, the 
        largest element in the array changes, then we record it
        """
        skyline = []
        heights = []
        maxHeap = []
        
        for b in buildings:
            if heights and heights[-1] == (b[0], b[2], "end"):
                # if the new start is the same as the last's end
                # do not add, and also remove the last entry
                heights = heights[0:len(heights) - 1]
            else:
                heights.append((b[0], b[2], "start"))
            heights.append((b[1], b[2], "end"))
        heights.sort()
        
        heapq.heapify(maxHeap)
        # heapq only has minHeaps, we need to insert negative element in
        # and we need to reverse the sign when getting an element out
        for i in range(len(heights)):
            currentMaxItem = -maxHeap[0] if maxHeap else 0     
            if heights[i][2] == "start":
                heapq.heappush(maxHeap, -heights[i][1])
            else:
                # heights[i][2] == 'end'
                maxHeap.remove(-heights[i][1])
                heapq.heapify(maxHeap)

            if not maxHeap:
                # means we are at a place with no buildings 
                # this could be the end of the array too
                skyline.append([heights[i][0], 0])
            elif -maxHeap[0] != currentMaxItem:
                if skyline and (skyline[-1][0] == heights[i][0]):
                    skyline[-1][1] = max(skyline[-1][1], heights[i][1])
                else:
                    skyline.append([heights[i][0], -maxHeap[0]])
                
        return skyline
                
            
        
        
        
        
        