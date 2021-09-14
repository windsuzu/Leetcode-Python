from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        return [list(p[::-1]) for p in zip(*matrix)]

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for level in range(n // 2):
            for i in range((n - level * 2) - 1):
                (
                    matrix[0 + level][i + level],
                    matrix[i + level][n - 1 - level],
                    matrix[n - 1 - level][n - 1 - level - i],
                    matrix[n - 1 - level - i][0 + level],
                ) = (
                    matrix[n - 1 - level - i][0 + level],
                    matrix[0 + level][i + level],
                    matrix[i + level][n - 1 - level],
                    matrix[n - 1 - level][n - 1 - level - i],
                )
