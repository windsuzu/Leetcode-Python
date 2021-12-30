from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        else:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            if target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        return False