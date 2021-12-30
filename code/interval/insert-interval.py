from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # the idea is to iterate through the "intervals" list
        # check if each "interval" overlaps with "newInterval"
        
        # if overlapping, we update the "newInterval" and keep iterating the list
        # if not overlappeing, then we will have 2 options:
        
        #   1. "interval" is before "newInterval", 
        #      then we add the "interval" to the result
        
        #   2. "interval" is after "newInterval", 
        #      then we can return "newInterval" + "intervals after newInterval"
        
        res = []
        
        for i, interval in enumerate(intervals):
            a1, a2 = interval
            b1, b2 = newInterval
            
            if a2 < b1:
                res.append(interval)
            elif b2 < a1:
                return res + [newInterval] + intervals[i:]
            else:
                newInterval = [min(a1,b1), max(a2, b2)]
        
        # b2 < a1 never executed, 
        # our "newInterval" should be the last interval
        res.append(newInterval)
        return res