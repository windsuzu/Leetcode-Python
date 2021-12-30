from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. use a hashtable to count the frequency of each number
        
        # 2. convert the hashtable to an array (length = len(nums)+1)
        #    index = count of number(s)
        
        # 3. return k frequent elements starting from the largest index
        
        # time = O(n) + O(n) + O(n) = O(n)
        
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        res = []
        
        for num in nums: count[num] += 1
        for n, c in count.items(): freq[c].append(n)
        
        for l in freq[::-1]:
            if l: res.extend(l)
            if len(res) == k: return res