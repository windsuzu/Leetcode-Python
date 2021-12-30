from typing import List


class Solution:
    # This is DFS
    def generateParenthesis(self, n: int) -> List[str]:
        # we stop recursion when "start > n" or "end > start"
        res = []

        def dfs(path="", start=0, end=0):
            if start == end == n:
                res.append(path)
                return
            if start > n or end > start:
                return
            dfs(path + "(", start + 1, end)
            dfs(path + ")", start, end + 1)

        dfs()
        return res

    # This is backtracking
    def generateParenthesis(self, n: int) -> List[str]:
        # if start < n, you can add "("
        # if end < start, you can add ")"
        res = []

        def dfs(path=[], start=0, end=0):
            if start == end == n:
                res.append("".join(path))
                return
            if start < n:
                path.append("(")
                dfs(path, start + 1, end)
                path.pop()
            if end < start:
                path.append(")")
                dfs(path, start, end + 1)
                path.pop()

        dfs()
        return res