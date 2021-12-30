from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = 0, 0
        for num in nums:
            if count == 0:
                major, count = num, 1
                continue
            
            count += 1 if major == num else -1
        return major