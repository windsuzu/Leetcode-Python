from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # The idea is whether we can find any subset
        # that forms the half-sum of "nums".
        subsum = {0}
        target = sum(nums) / 2
        for num in nums:
            subsum.update({num + s for s in subsum})
            if target in subsum:
                return True
        return False