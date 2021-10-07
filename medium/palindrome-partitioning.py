from typing import List


class Solution:
    @staticmethod
    def is_palindrome(s: str):
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        output = []

        def dfs(i, path):
            if i == len(s):
                output.append(path)
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s[i : j + 1]):
                    dfs(j + 1, path + [s[i : j + 1]])

        dfs(0, [])
        return output