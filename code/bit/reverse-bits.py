class Solution:
    def reverseBits(self, n: int) -> int:
        # we can take the last bit of "n" by doing "n % 2"
        # and shift the "n" to the right
        
        # then we paste the last bit to the first bit of "res" 
        # by using `|` operation
        
        # Take 0101 as an example:
        # 0010 (1) => 1 000
        # 0001 (0) => 10 00
        # 0000 (1) => 101 0
        # 0000 (0) => 1010
        
        res = 0
        for i in range(32):
            bit = n % 2
            n >>= 1
            # res += 2 ** (31-i) if bit else 0
            res |= bit << (31-i)
        
        return res