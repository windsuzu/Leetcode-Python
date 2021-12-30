from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i=0, total=0):
            if i == len(nums):
                return total == target

            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[(i, total)]

        return dfs()