from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the idea is to loop through all the cells
        # if we find any "1", then we DFS from it to all its adjancent cells
        # and mark the cell as visited by replacing "1" with "v"
        
        # once we are done with one island, 
        # we can continue with "1" scan
        
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] in "0v":
                return
            grid[i][j] = "v"
            
            dfs(i-1, j)  # top
            dfs(i+1, j)  # down
            dfs(i, j-1)  # left
            dfs(i, j+1)  # right
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res