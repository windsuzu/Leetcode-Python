from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the idea is to use a "character counter" to track acceptable substring length
        # the acceptable substring length is equal to
        # len(substring) - max(character count)
        # e.g. "BBBA" = 4 - 3 = 1

        counter = defaultdict(int)
        l, r, res = 0, 0, 0
        
        while r < len(s):
            counter[s[r]] += 1
            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            r += 1
        return res
            