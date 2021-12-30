from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # After sorting the elements, duplicated elements will be placed next to each other.
        output = []
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                output.append(nums[i])

        return output

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        # list comprehension
        nums.sort()
        return [nums[i] for i in range(len(nums) - 1) if nums[i] == nums[i + 1]]
