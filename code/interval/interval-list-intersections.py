from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            i_s, i_e = firstList[i]
            j_s, j_e = secondList[j]

            # check intersection
            if i_s <= j_e and j_s <= i_e:
                res.append([max(i_s, j_s), min(i_e, j_e)])

            # move the pointer with smaller [end] value forward
            i += i_e <= j_e
            j += j_e < i_e

        return res
