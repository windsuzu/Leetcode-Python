class Solution:
    def backspaceCompareStack(self, s: str, t: str) -> bool:
        def process(word):
            stack = []
            for c in word:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return process(s) == process(t)
    
    
    def backspaceComparePointers(self, s: str, t: str) -> bool:
        ps, pt = len(s)-1, len(t)-1
        counts, countt = 0, 0
        
        while True:
            while ps >= 0 and (counts or s[ps] == "#"):
                counts += 1 if s[ps] == "#" else -1
                ps -= 1
            
            while pt >= 0 and (countt or t[pt] == "#"):
                countt += 1 if t[pt] == "#" else -1
                pt -= 1
            
            if not (ps >= 0 and pt >= 0 and s[ps] == t[pt]):
                return ps == pt == -1
            
            ps, pt = ps-1, pt-1