from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We can use "low" to maintain the minimum value 
        # and use "res" to maintain the maximum profit
        
        res = 0
        low = prices[0]
        
        for price in prices[1:]:
            if price - low > 0:
                res = max(res, price - low)
            else:
                low = price
        
        return res