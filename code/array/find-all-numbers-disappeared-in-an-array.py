from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # the idea is to update list in-place to
        # mark the number in the index corresponding to the current "num"
        
        for num in nums:
            i = abs(num) - 1
            nums[i] = -abs(nums[i])
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        