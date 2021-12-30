from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            
            # if "num" exists in the dictionary 
            # then returning the current index and dictionary index
            
            if num in d:
                return [i, d[num]]
            
            # save "target-num" into dictionary
            else:
                d[target - num] = i