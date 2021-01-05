'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

'''

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        self.grid = grid
        
        def dfs(point):
            r, c = point
            # if point is invalid return nothing
            if r < 0 or c < 0 or r > len(self.grid)-1 or c > len(self.grid[0]) -1 or self.grid[r][c] == 1:
                return
            
            self.grid[r][c] = 1
            
            up = dfs((r-1, c))
            right = dfs((r, c+1))
            down = dfs((r+1, c))
            left = dfs((r, c-1))
            
            minR = min(r, up[0] if up else r, right[0] if right else r, down[0] if down else r, left[0] if left else r)
            minC = min(c, up[1] if up else c, right[1] if right else c, down[1] if down else c, left[1] if left else c)
            maxR = max(r, up[2] if up else r, right[2] if right else r, down[2] if down else r, left[2] if left else r)
            maxC = max(c, up[3] if up else c, right[3] if right else c, down[3] if down else c, left[3] if left else c)
            
            return (minR, minC, maxR, maxC)
        
        closedIslands = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] ==  0:
                    minR, minC, maxR, maxC = dfs((r, c))
                    if minR > 0 and minC > 0 and maxR < len(self.grid)-1 and maxC < len(self.grid[0])-1:
                        closedIslands += 1
        return closedIslands
            
