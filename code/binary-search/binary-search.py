from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if nums[m] > target: r = m - 1
            else: l = m + 1
        return -1
    
    def search_bisect(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        return (i if i < len(nums)     # prevent target > all elements
                and nums[i] == target  # prevent target < all elements
                else -1)