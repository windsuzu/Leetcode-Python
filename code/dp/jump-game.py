from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # the idea is to use DP and loop through "nums" reversely
        
        # the base case is the "last position", 
        # this means if we are at the last position, 
        # we can win the jump game
        
        goal = len(nums)-1
        
        # we will check if each of the previous positions can be a new "goal"
        # by checking if we can jump from each position to the old "goal"
        
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0