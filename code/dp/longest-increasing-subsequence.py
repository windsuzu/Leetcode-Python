from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We can use binary search to replace the leftmost element
        # that is just larger than the new value
        
        res = []
        for num in nums:
            if res and num <= res[-1]:
                i = bisect.bisect_left(res, num)
                res[i] = num
            else:
                res.append(num)
        return len(res)