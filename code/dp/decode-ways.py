class Solution:
    def numDecodings(self, s: str) -> int:
        # The idea is to use DP and iterate "s" reversely
        # we set "dp[len(s)] = 1" which means the string is fully decoded
        
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        
        # there are 2+1 cases we need to handle when hitting a new digit:
        
        # 1. when s[i] equals 0, we set dp[i] = 0
        
        # 2. when s[i] is 1-9, we set dp[i] = dp[i+1]
        #    which not only means we accept s[i]
        #    but we also wanna check how many combinations after s[i]
        
        # 3. s[i: i+2] is in 10-26, we set dp[i] += dp[i+2]
        #    lastly, if s[i] can be expanded to two digits
        #    we add the number of combinations from dp[i+2]
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if i + 1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
            
        return dp[0]