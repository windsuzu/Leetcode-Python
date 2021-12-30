from typing import List
from collections import defaultdict


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dfs(target):
            if target <= 0:
                return target == 0

            if target in memo:
                return memo[target]

            for num in nums:
                memo[target] += dfs(target - num)

            return memo[target]

        return dfs(target)
