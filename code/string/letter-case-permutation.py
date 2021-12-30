from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(i=0, path=""):
            if i == len(s):
                res.append(path)
                return

            if s[i].isnumeric():
                dfs(i + 1, path + s[i])
            else:
                dfs(i + 1, path + s[i].lower())
                dfs(i + 1, path + s[i].upper())

        dfs()
        return res