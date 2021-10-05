from typing import List

class Solution:
    def findTargetSumWays_bruteforce(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)

        def dfs(nums, path):
            nonlocal count
            if sum(path) == target and len(path) == n:
                count += 1
            
            if len(nums) == 0:
                return
            
            dfs(nums[1:], path + [nums[0]])
            dfs(nums[1:], path + [-nums[0]])

        dfs(nums, [])
        return count
    
    
    def findTargetSumWays_memo(self, nums: List[int], target: int) -> int:
        mem = {}
        
        def dfs(index, s):
            if index == len(nums):
                return s == target
            
            if (index, s) in mem:
                return mem[(index, s)]

            mem[(index, s)] = dfs(index+1, s+nums[index]) + \
                              dfs(index+1, s-nums[index])

            return mem[(index, s)]
        
        return dfs(0, 0)