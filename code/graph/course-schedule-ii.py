from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a hashtable indicates prerequisites for each course
        # e.g. [[1,0]] = {0: [], 1: [0]}
        table = {i: [] for i in range(numCourses)}
        for (a, b) in prerequisites:
            table[a].append(b)

        res, visit, cycle = [], set(), set()

        # use DFS to unravel prerequisites and detect cycle
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True

            cycle.add(i)
            for pre in table[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)

            visit.add(i)
            res.append(i)

            return True

        # scan every single course
        for i in range(numCourses):
            if not dfs(i):  # has cycle
                return []

        return res