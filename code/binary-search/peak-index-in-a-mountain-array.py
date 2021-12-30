from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # use binary search to search peak index
        l, r = 0, len(arr)-1
        
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m+1]:  # mid < peak
                l = m + 1
            else:
                r = m  # peak <= mid
        return l