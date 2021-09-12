from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    rows.add(i)
                    cols.add(j)

        for i, row in enumerate(matrix):
            if i in rows:
                matrix[i] = [0] * len(matrix[i])
                continue
                
            for j, element in enumerate(row):
                if j in cols:
                    matrix[i][j] = 0