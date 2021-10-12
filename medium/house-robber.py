from typing import List
from collections import deque

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])
        elif len(nums) == 3: return max(nums[0] + nums[2], nums[1])
        
        l = deque([nums[0], nums[1], nums[0] + nums[2]])
        
        for num in nums[3:]:
            l.append(max(num+l.popleft(), num+l[0]))
        
        return max(l)