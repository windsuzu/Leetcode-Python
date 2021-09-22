from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(candidates, target, path):
            if target < 0:
                return
            elif target == 0:
                output.append(path)
            else:
                for i in range(len(candidates)):
                    dfs(candidates[i:], target - candidates[i], path + [candidates[i]])

        dfs(candidates, target, [])
        return output