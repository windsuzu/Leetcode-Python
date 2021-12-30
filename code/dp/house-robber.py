from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # The idea is to use DP and iterate from the first house to the last
        
        # But we only need to maintain two variables: "dp1", "dp2"
        # [dp2, dp1, now, now+1, ...]
        # [ - , dp2, dp1, now, ...]
        
        # And there will only be two subproblems:
        # 1. now + dp1
        # 2. max(dp1 | dp2)
        
        dp1 = dp2 = 0
        for now in nums:
            dp1, dp2 = max(now+dp2, dp1), dp1
        return dp1