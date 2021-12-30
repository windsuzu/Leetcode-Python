from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The idea is to remove any negative prefix "pre" when we loop through the "nums"
        # because the negative prefix won't help
        # and we use "res" to maintain the sum of maximum subarray
        
        res, pre = nums[0], nums[0]
        
        for num in nums[1:]:
            if pre < 0:
                pre = 0
            pre += num
            res = max(res, pre)
        return res