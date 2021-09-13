from typing import List
from itertools import chain
import math


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def circulate(lv=0):
            i, j = lv, lv
            temp = []

            # first row (++col)
            if j == len(matrix[0]) - lv:
                return temp

            for j in range(j, len(matrix[0]) - lv):
                temp.append(matrix[i][j])

            # last col (++row)
            if i + 1 == len(matrix) - lv:
                return temp

            for i in range(i + 1, len(matrix) - lv):
                temp.append(matrix[i][j])

            # last row (--col)
            if j - 1 == lv - 1:
                return temp

            for j in range(j - 1, lv - 1, -1):
                temp.append(matrix[i][j])

            # first col (--row)
            if i - 1 == lv:
                return temp

            for i in range(i - 1, lv, -1):
                temp.append(matrix[i][j])
            return temp

        num = math.ceil(min(len(matrix), len(matrix[0])) / 2)
        return list(chain.from_iterable([circulate(i) for i in range(num)]))
