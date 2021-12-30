from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # the idea is to sort the intervals in ascending order 
        # by the "start" of each interval
        
        intervals.sort(key=lambda x: x[0])
        
        # if current interval overlaps with pervious one,
        # then we can update the previous interval's end
        # for example: [1, 4], [2, 5] -> update 4 with "max(4, 5)" -> [1, 5]
        
        # if there's no overlap
        # then we can simply put the current interval into result 
        
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= res[-1][-1]:  # overlap
                res[-1][-1] = max(end, res[-1][-1])
            else:  # no overlap
                res.append([start, end])
        return res