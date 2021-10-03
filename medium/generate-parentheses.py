from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []

        def dfs(path, left, right):
            if left == n and right == n:
                output.append(path)
            elif right > left or left > n or right > n:
                return

            dfs(path + "(", left + 1, right)
            dfs(path + ")", left, right + 1)

        dfs("", 0, 0)
        return output