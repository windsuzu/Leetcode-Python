from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can first create an array to put prefixes into it 
        # and loop backward the "nums" again to multiply prefixes with postfixes
        
        arr = [1]
        pre, post = 1, 1
        
        for i in range(len(nums) - 1):
            pre *= nums[i]
            arr.append(pre)
        
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= post
            post *= nums[j]
        
        return arr
        
