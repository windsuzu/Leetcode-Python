class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # The idea is to use 2D dynamic programming from the top-left
        
        # if the characters are match, 
        # we set the cell = 1 + top-left
        
        # if the characters aren't match, 
        # we set the cell = max(top or left)
        
        dp = [[0 for _ in range(len(text2))] 
                 for _ in range(len(text1))]
        
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (dp[i-1][j-1] if (i > 0 and j > 0) else 0)
                else:
                    dp[i][j] = max(dp[i-1][j] if i > 0 else 0, 
                                   dp[i][j-1] if j > 0 else 0)
        
        return dp[-1][-1]
