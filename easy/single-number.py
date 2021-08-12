from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z = nums[0]
        for num in nums[1:]:
            z^= num
        return z
        