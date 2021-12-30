from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Starting from 1, the number of bits will be 1 + dp[i-offset]
        # where the offset will double up whenever we hit a new heading bit (1,2,4,8,16,...)
        # For example:
        # 000
        # 001 = 1 + dp[1 - 1]
        # 010 = 1 + dp[2 - 2]
        # 011 = 1 + dp[3 - 2]
        # 100 = 1 + dp[4 - 4]
        # 101 = 1 + dp[5 - 4]
        
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
                
            dp[i] = 1 + dp[i-offset]
            
        return dp