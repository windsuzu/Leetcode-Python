from typing import List


# O(mlogn)
class Solution:
    def search(self, arr, target):
        l, r = 0, len(arr)
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            elif arr[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) and target >= matrix[row][0]:
            if target <= matrix[row][-1] and self.search(matrix[row], target):
                return True
            else:
                row += 1
        return False


# O(m + n)
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the idea is searching from the top-right
        # if target < element: search left, because all elements in same col is bigger than target
        # if target > element: search below, because all elements in same row is less than taget
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False