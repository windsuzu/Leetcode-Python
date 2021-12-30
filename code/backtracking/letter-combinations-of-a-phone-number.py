from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i=0, path=[]):
            if i == len(digits):
                res.append("".join(path))
                return

            for c in l[digits[i]]:
                path.append(c)
                dfs(i + 1, path)
                path.pop()

        dfs()
        return res if digits else []