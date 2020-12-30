'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
'''

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        
        # start a DFS from each of the points, and you count the numbers of 1s in the chain
        if not grid or not grid[0]:
            return 0
        
        self.grid = grid
        maxSize = 0
        
        def dfs(point):
            r, c = point
            
            if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]) or self.grid[r][c] == 0:
                return 0
            else:
                self.grid[r][c] = 0
                
            return dfs((r-1,c)) + dfs((r+1,c)) + dfs((r,c-1)) + dfs((r,c+1)) + 1
        
#             islandSize = 0
#             stack = [point]
#             while stack:
#                 r, c = stack[-1]
                
#                 if self.grid[r][c] == 1:
#                     self.grid[r][c] = 0
#                     islandSize += 1
                
#                 neighbor = getNeighbor((r, c)) # dont check if the current element is 0
#                 if neighbor: stack.append(neighbor)
#                 else: stack.pop()

#             return islandSize
        
        # def getNeighbor(point):
        #     r, c = point
        #     # up
        #     if r > 0 and self.grid[r-1][c] == 1:
        #         return (r-1, c)
        #     # down
        #     if r < len(self.grid) - 1 and self.grid[r+1][c] == 1:
        #         return (r+1, c)
        #     # left
        #     if c > 0 and self.grid[r][c-1] == 1:
        #         return (r, c-1)
        #     # down
        #     if c < len(self.grid[0]) - 1 and self.grid[r][c+1] == 1:
        #         return (r, c+1)
        #     # None
        #     return None
        
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    maxSize = max(maxSize, dfs((r, c)))
        
        return maxSize
                