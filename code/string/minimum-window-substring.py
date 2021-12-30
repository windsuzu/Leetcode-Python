from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first, find the reasonable minimum substring by brute force
        
        l, r,  = 0, 0
        res, res_min = "", float("inf")
        
        count_t, count_s = defaultdict(int), defaultdict(int)
        have = 0
        
        for c in t:
            count_t[c] += 1
        
        while r < len(s):
            count_s[s[r]] += 1
            
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have += 1

            # after the first several loops, we will get a valid substring
            
            while have == len(count_t):
                if (r - l + 1) < res_min:
                    res_min = (r - l + 1)
                    res = s[l:r+1]
                    
                # contract the substring while meeting the condition
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
                
            # expand the substring while not meeting the condition
            r += 1
        return res