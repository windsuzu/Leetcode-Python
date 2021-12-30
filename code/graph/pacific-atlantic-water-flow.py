from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # the idea is to apply DFS on every cell
        # that already belongs to Pacific or Atlantic ocean
        # that is, the first row and first column, last row and last column
        
        # by DFS from 4 directions, we will have 2 sets
        # the first set contains cells belonging to pacific
        # the second set contains cells belonging to atlantic
        # and we can find the intersection of 2 sets as our answer
    
        pac, atl = set(), set()
        m, n = len(heights), len(heights[0])
        
        def dfs(i, j, prev_h, visited):
            if i < 0 or j < 0 or i == m or j == n \
            or (i, j) in visited or heights[i][j] < prev_h:
                return
            visited.add((i, j))
            
            dfs(i-1, j, heights[i][j], visited)  # top            
            dfs(i+1, j, heights[i][j], visited)  # down            
            dfs(i, j-1, heights[i][j], visited)  # left            
            dfs(i, j+1, heights[i][j], visited)  # right  
            
        for i in range(m):
            dfs(i, 0, heights[i][0], pac) # first column
            dfs(i, n-1, heights[i][n-1], atl)  # last column
            
        for j in range(n):
            dfs(0, j, heights[0][j], pac) # first row
            dfs(m-1, j, heights[m-1][j], atl) # last row
        
        return pac.intersection(atl)