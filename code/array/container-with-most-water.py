from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # We can create "left" and "right" pointers
        # the initial width between "l" and "r" is already the maximum
        
        l, r = 0, len(height) - 1
        width = r - l
        
        # We can use greedy method to move the lower line to the next line
        # For example, if height[l] < height[r], then we move "l" to "l+1"
        # if height[l] > height[r], then we move "r" to "r-1"
        # if they are the same, then it's ok to move either one
        
        res = 0
        
        while l < r:
            res = max(res, width * min(height[l], height[r]))
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            
            width -= 1
            
        return res