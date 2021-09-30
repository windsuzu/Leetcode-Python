from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def dfs(path, target, start):
            if target <= 0:
                if target == 0:
                    output.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                dfs(path + [candidates[i]], target - candidates[i], i + 1)

        dfs([], target, 0)
        return output