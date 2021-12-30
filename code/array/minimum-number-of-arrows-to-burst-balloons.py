from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # the idea is to sort the list by "x_end"
        # if the "x_start" of a new point is smaller
        # than the "x_end" of the previous one
        # then they can be shot by 1 arrow
        points.sort(key=lambda x: x[1])
        res = 1
        last_end = points[0][1]

        for x_start, x_end in points[1:]:
            if x_start > last_end:
                res += 1
                last_end = x_end

        return res