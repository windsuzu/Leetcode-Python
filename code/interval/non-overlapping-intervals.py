from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # we can first sort the "intervals" by "start" positions O(nlogn)
        intervals.sort(key=lambda x: x[0])
        
        # then we iterate through the list O(n)
        # with an minimum "end" pointer
        
        # if the current one overlaps with the previous one
        # i.e., current.start < previous.end
        # then we can increase the counter by 1
        
        # also, we have to keep updating the previous one's end by
        # "min(previous.end, current.end)"
        
        min_end = intervals[0][1]
        res = 0
        
        for start, end in intervals[1:]:
            if start < min_end:
                res += 1
                min_end = min(min_end, end)
            else:
                min_end = end
        return res