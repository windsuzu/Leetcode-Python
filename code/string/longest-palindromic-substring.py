class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the idea is to use two pointers on each position
        # we will search the palindrome in expanded way
        # e.g. (b) <- (a) <- (c) -> (a) -> (b)

        start, max_len = 0, 1
        
        for i in range(len(s)):
            # expand the right side, e.g. "b[a]ab": i=1, l=0, r=3
            r = i
            l = i - 1
            while r < len(s) and s[i] == s[r]:
                r += 1
            
            # expand both sides, e.g. "b[a]ab": l=-1, r=4 cuz s[0] == s[3]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            
            # store the max_len
            if (r - l - 1) > max_len:
                max_len = (r - l - 1)
                start = l + 1
        
        return s[start: start + max_len]