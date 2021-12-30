from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The idea is to use "set(nums)" as a hashtable
        
        # we can find out if the num is the first element of a consecutive sequence (cs)
        # by checking if "num - 1 not in set"
        
        # if the num is the first element of a cs,
        # then we can keep checking the elements after it
        
        table = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in table:
                count = 1
                while num + 1 in table:
                    count += 1
                    num += 1
                res = max(res, count)
        return res