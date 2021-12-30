from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use binary search, so we have 3 vars: "left", "mid", "right"
        
        # First, we need to know where the "mid" is in the left ascending zone or right ascending zone
        
        # Second, if "mid" is in the left zone, there will be three options:
        # if "target" > "mid": search the right side
        # if "target" < "mid" but also "target" < "left": search the right side
        # else: we search the left side.
        
        # Third, if "mid" is in the right zone, there will also be three options:
        # if "target" < "mid" : search the left side
        # if "target" > "mid" but "target" > "right": search the left side
        # else: we search the right side
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # in the left side
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: r = m - 1
                else: l = m + 1
                    
            # in the right side
            else:
                if nums[m] < target <= nums[r]: l = m + 1
                else: r = m - 1
                
        return -1