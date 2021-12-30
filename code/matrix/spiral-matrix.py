from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # the idea is to use 4 pointers (top, bottom, left, right)
        # to detect whether we are iterating over the last row or column
        
        t, b, l, r = 0, len(matrix), 0, len(matrix[0])
        res = []
        while t < b and l < r:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            
            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
            
            # already iterated over the last row or last column
            if t == b or l == r: break
            
            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b -= 1
            
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res