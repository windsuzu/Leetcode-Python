from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) => int:
        sum_full = int(((len(nums) + 0 ) * (len(nums) + 1)) / 2)
        sum_loss = sum(nums)
        return sum_full - sum_loss