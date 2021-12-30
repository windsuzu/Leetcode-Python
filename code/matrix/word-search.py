from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # the idea is to use DFS on each cell
        
        m, n = len(board), len(board[0])
        seen = set()
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            
            if (i < 0 or j < 0 or i == m or j == n or
                board[i][j] != word[index] or (i, j) in seen):
                return False
            
            seen.add((i, j))
            res = (dfs(i-1, j, index+1) or
                   dfs(i+1, j, index+1) or
                   dfs(i, j-1, index+1) or
                   dfs(i, j+1, index+1))
            seen.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False