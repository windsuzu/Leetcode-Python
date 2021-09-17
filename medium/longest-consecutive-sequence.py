from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        i, max_count = 0, 1
        while i < len(nums):
            count = 1
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                count += 1
                i += 1
            i += 1
            max_count = max(max_count, count)
        return max_count if nums else 0