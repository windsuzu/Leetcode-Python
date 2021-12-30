from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # the idea is to use two pointers (l, r) to indicate 
        # which cycle we are currently rotating
        
        l, r = 0, len(matrix)-1
        
        while l < r:
            t, b = l, r
            for i in range(0, r - l):
                tmp = matrix[t][l+i]  # top-left element
                matrix[t][l+i] = matrix[b-i][l]  # top-left < bottom-left
                matrix[b-i][l] = matrix[b][r-i]  # bottom-left < bottom-right
                matrix[b][r-i]= matrix[t+i][r]  # bottom-right < top-right
                matrix[t+i][r] = tmp  # top-right < top-left
            
            l, r = l+1, r-1