from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the idea is to run a topological sort with cycle detection
        # we use a "seen" set to store visited nodes
        
        # after we finish the topological sort
        # and there is no cycle in our graph, then we return true
        
        graph = {i: [] for i in range(numCourses)}
        seen = set()
        
        # [[1, 0], [2, 0]] -> {0: [], 1: [0], 2: [0]}
        for (course, pre) in prerequisites:
            graph[course].append(pre)
        
        def dfs(node):
            if not graph[node]:
                return True
            elif node in seen:
                return False
            
            seen.add(node)
            for neig in graph[node]:
                if not dfs(neig): return False
            seen.remove(node)
            graph[node] = []
            return True
        
        return all([dfs(node) for node in range(numCourses)])
            
            
            
            
            
        
