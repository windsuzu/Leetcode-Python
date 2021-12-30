from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The idea is to use dp from the end to the beginning
        # The base case is "dp[len(s)+1] = True"
        
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]
        