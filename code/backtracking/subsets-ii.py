from typing import List


class Solution:
    # use set to avoid duplicates
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def dfs(index=0, path=[]):
            for i in range(index, len(nums) + 1):
                if i == len(nums):
                    res.add(tuple(path))
                    return
                dfs(i + 1, path + [nums[i]])

        dfs()
        return res

    # compare "current value" and "last element in the path" to avoid duplicates
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, path = [], []

        def dfs(i=0):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            if not path or nums[i] != path[-1]:
                dfs(i + 1)

        dfs()
        return res