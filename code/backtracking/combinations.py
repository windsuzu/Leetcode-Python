from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(index=1, path=[]):
            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(index, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs()
        return res