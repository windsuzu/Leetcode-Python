from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
		
		# find the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
		# find the starting point of the cycle
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return start