from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        
        def check(i, j, visited, pos=0):
            if pos == len(word):
                return True
            
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
                return False
            
            visited[(i, j)] = True
            res = check(i, j + 1, visited, pos + 1) \
                    or check(i, j - 1, visited, pos + 1) \
                    or check(i + 1, j, visited, pos + 1) \
                    or check(i - 1, j, visited, pos + 1)
            visited[(i, j)] = False
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, visited):
                    return True
        return False