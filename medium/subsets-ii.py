from typing import List
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return {
            tuple(sorted(s))
            for i in range(len(nums) + 1)
            for s in combinations(nums, i)
        }
