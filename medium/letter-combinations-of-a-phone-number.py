from typing import List
from itertools import product

class Solution:
    def letterCombinations_product(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return ["".join(c) for c in product(*[d[i] for i in digits])] if digits else []
    
    
    def letterCombinations_backtracking(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        output = []
        source = [d[i] for i in digits]
        
        def dfs(i, path):
            if len(path) == len(digits):
                if path:
                    output.append(path)
                return
            
            for j in range(0, len(source[i])):
                dfs(i + 1, path + source[i][j])
            
        dfs(0, "")
        return output
