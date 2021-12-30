class Solution:
    def hammingWeight(self, n: int) -> int:
        # when the last bit is 1, "n % 2" will return 1
        # and we shift all the bit to the right until "n == 0"
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res
    
    
    def hammingWeight2(self, n: int) -> int:
        # Every time "n & n-1" operation will remove the rightmost 1
        # Take 10011 as an example:
        # 10011 & 10010 = 10010 (res+1)
        # 10010 & 10001 = 10000 (res+1)
        # 10000 & 01111 = 00000 (res+1)
        res = 0
        while n:
            n &= n-1
            res += 1
        return res