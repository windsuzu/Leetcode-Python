from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we can use binary search, and use "res" to maintain the minimum value
        
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        while l <= r:
            # if the rightmost is bigger than the leftmost
            # then the elements between l and r must be in ascending
            # and we can simply return the leftmost
            
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            
            # if the middle is larger than the leftmost
            # then we can focus on right side
            # and vice versa
            
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        return res