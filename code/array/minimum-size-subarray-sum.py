from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, csum, res = 0, 0, float("inf")

        for i, val in enumerate(nums):
            csum += val
            while csum >= target:
                res = min(res, i - left + 1)
                csum -= nums[left]
                left += 1

        return res if res != float("inf") else 0