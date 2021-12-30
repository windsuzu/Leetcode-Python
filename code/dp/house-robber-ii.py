from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # the idea is to reuse the code from House Robber I
        
        def helper(nums):
            # [dp1, dp2, num, num+1, ...]
            
            dp1 = dp2 = 0
            for num in nums:
                dp1, dp2 = dp2, max(num+dp1, dp2)
            return dp2
        
        # because we are not allowed to rob "first + last" house at the same time
        # so we can try to rob without first, and rob without last
        # and compute max(rob_without_first | rob_without_last)
        
        # also, remember to include `nums[0]`
        # to prevent the edge case when "len(nums) == 1"
        
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])