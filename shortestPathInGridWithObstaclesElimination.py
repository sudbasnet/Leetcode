'''
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). 
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) 
to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. 
If it is not possible to find such walk return -1.
'''


class Solution:
    def shortestPath(self, grid, k) -> int:
        if not grid or not grid[0]:
            return -1

        self.paths = {}  # for memoization
        self.grid = grid  # making it accessible to anywhere inside the class

        def dfs(start, k, visited):
            r, c = start

            if (start, k) in self.paths:
                return self.paths[(start, k)]

            # invalid node
            if r < 0 or r > len(self.grid)-1 or c < 0 or c > len(self.grid[0])-1 or (r, c) in visited:
                return float('inf')

            # update k
            if self.grid[r][c] == 1 and k == 0:
                return float('inf')
            k -= 1 if self.grid[r][c] == 1 else 0

            # if valid manhattan path
            if k >= len(self.grid) + len(self.grid[0]) - 3 - r - c:
                self.paths[(start, k)] = len(self.grid) + \
                    len(self.grid[0]) - 2 - r - c
                return self.paths[(start, k)]

            # else check neighbors
            up, down = dfs((r-1, c), k, visited +
                           [(r, c)]), dfs((r+1, c), k, visited + [(r, c)])
            left, right = dfs((r, c-1), k, visited +
                              [(r, c)]), dfs((r, c+1), k, visited + [(r, c)])

            # momoize
            self.paths[(start, k)] = 1 + min(up, down, left, right)
            return self.paths[(start, k)]

        minPath = dfs((0, 0), k, [])
        if minPath == float('inf'):
            return -1
        return minPath
