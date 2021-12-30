from typing import List


class Solution:
    # use hashset to skip numbers that have already appeared
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, seen = [], set()

        def dfs(path=[]):
            if len(path) == len(nums):
                res.append(path)
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    dfs(path + [nums[i]])
                    seen.remove(i)

        dfs()
        return res

    # use list slicing to skip numbers
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :], path + [nums[i]])

        dfs(nums)
        return res