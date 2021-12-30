from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(index=0, path=[], total=0):
            if total == target:
                res.append(path.copy())
                return

            if index >= len(candidates) or total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        dfs()
        return res