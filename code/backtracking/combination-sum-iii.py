from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(index=1, path=[], total=0):
            if total == n and len(path) == k:
                res.append(path.copy())
                return

            if index > 9 or total > n or len(path) > k:
                return

            for i in range(index, 10):
                path.append(i)
                dfs(i + 1, path, total + i)
                path.pop()

        dfs()
        return res