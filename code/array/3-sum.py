from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We can first sort the array (O nlogn), and say we want to acheieve a+b+c=0
        # We can lock the "a" and solve the TwoSum problem with target="-a" (O n) 
        # And if "a" is >= 1, we can finish the problem        
        # After we finish the "a", we have to jump to the last "a" if there are duplicate "a"s
        
        # For the two sum problem, we can use "left" and "right" pointers
        # if the sum is bigger than "-a", we move "right" - 1
        # if the sum is less than "-a", we move "left" + 1
        
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] >= 1:
                break
            
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
