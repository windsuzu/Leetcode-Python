from typing import List

class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        nums = set(nums)
        output = []
        
        for i in range(1, n):
            if i not in nums:
                output.append(i)
        
        return output
    
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1))-set(nums))
    