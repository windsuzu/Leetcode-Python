from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep update both "min" and "max" to current position
        # And use "res" to maintain the maximum product 
        
        res = maxC = minC = nums[0]
        
        for num in nums[1:]:
            tempMaxC = max(num*maxC, num*minC, num)
            minC = min(num*maxC, num*minC, num)
            maxC = tempMaxC
            res = max(maxC, res)
        
        return res
    
        # for example
        # [2 3 0 -2 -4]
        # max min res
        #   2   2   2
        #   6   3   6
        #   0   0   6
        #   0  -2   6
        #   8  -4   8