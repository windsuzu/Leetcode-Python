class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the idea is to use "set" and "two pointers" to implement sliding window
        
        sub = set()
        l, r, res = 0, 0, 0
        
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
                
            sub.add(s[r])
            r += 1
            res = max(res, r - l)
        
        return res