from typing import List


class Solution:
    def ispalindrome(self, s):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(index=0, path=[]):
            if index == len(s):
                res.append(path.copy())
                return

            for i in range(index, len(s)):
                if self.ispalindrome(s[index : i + 1]):
                    path.append(s[index : i + 1])
                    dfs(i + 1, path)
                    path.pop()

        dfs()
        return res