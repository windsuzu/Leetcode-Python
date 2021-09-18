from typing import List
from itertools import chain, combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(nums, i) for i in range(len(nums)+1))
