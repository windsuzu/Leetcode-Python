from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[r]:
                r -= 1  # or "r -= 1"

            m = (l + r) // 2
            if nums[m] == target:
                return True

            if nums[l] <= nums[m]:  # left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # right side is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False