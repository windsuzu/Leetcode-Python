class Solution:
    def isValid(self, s: str) -> bool:
        # the idea is to use a stack and a fixed hashtable
        stack = []
        check = { ")": "(", "}": "{", "]": "[" }
        
        for c in s:
            if c in check:
                if stack and check[c] == stack.pop():
                    continue
                return False
            else:
                stack.append(c)
        return not stack