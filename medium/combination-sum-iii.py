from typing import List
from itertools import combinations


class Solution:
    def combinationSum3_1liner(self, k: int, n: int) -> List[List[int]]:
        return [c for c in combinations([i for i in range(1, 10)], k) if sum(c) == n]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []

        def dfs(path, start):
            if len(path) == k and sum(path) == n:
                output.append(path)
            elif len(path) >= k or sum(path) >= n:
                return
            for i in range(start, 9):
                dfs(path + [i + 1], i + 1)

        dfs([], 0)
        return output

