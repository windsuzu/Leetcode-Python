class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            r = i
            l = i - 1
            
            while r < len(s) and s[i] == s[r]:
                r += 1
                res += 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
                
        return res