from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        acc = nums[0]
        history_min = nums[0]
        
        for num in nums[1:]:
            acc += num
            result = max(result, acc, acc - history_min)
            history_min = min(acc, history_min)

        return result
    