from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we can sum up range [0, max] `(full)` 
		# and subtract the sum of the input list `(loss)`
        full = int(((len(nums) + 0 ) * (len(nums) + 1)) / 2)
        loss = sum(nums)
        return full - loss
    
    
    def missingNumber2(self, nums: List[int]) -> int:
        # we can use XOR operation through both full and loss nums
		# For example: [1,0,3] and [0,1,2,3]
		#   1 ^ 0 ^ 3 ^ 0 ^ 1 ^ 2 ^ 3
		# = 0 ^ 0 ^ 1 ^ 1 ^ 2 ^ 3 ^ 3 
		# = 2
        res = 0
        for i in range(len(nums)):
            res ^= i+1 ^ nums[i]
        return res