from typing import List
from collections import Counter


class Solution:
    # Implement with a counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        count = Counter(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    path.append(num)
                    dfs()
                    path.pop()
                    count[num] += 1

        dfs()
        return res

    # Implement with sort and (i, i-1) comparision
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[:i] + nums[i + 1 :], path + [nums[i]])

        dfs(nums)
        return res