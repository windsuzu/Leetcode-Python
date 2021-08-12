from typing import List
import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0, 1]
        if n > 1:
            iterations = math.floor(math.log2(n))
            for _ in range(iterations):
                arr.extend([c+1 for c in arr])
        
        return arr[:n+1]
        