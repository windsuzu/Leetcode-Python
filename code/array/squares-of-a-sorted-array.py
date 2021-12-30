from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # the idea is to use two pointers to put the larger square value into result
        l, r = 0, len(nums)-1
        res = [0] * len(nums)
        while l <= r:
            if (a:= nums[l] ** 2) >= (b:=nums[r] ** 2):
                res[r - l] = a
                l += 1
            else:
                res[r - l] = b
                r -= 1
        return res