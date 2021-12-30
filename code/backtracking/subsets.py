from typing import List


class Solution:
    # use a for-loop
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index=0, path=[]):
            for i in range(index, len(nums) + 1):
                if i == len(nums):
                    res.append(path)
                    return
                dfs(i + 1, path + [nums[i]])

        dfs()
        return res

    # use pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(i=0):
            if i == len(nums):
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)

        dfs()
        return res