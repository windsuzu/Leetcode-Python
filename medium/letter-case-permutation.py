class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [s[0]] if s[0].isdigit() else [s[0].lower(), s[0].upper()]
        for c in s[1:]:
            if c.isdigit():
                output = [out + c for out in output]
            else:
                output = [
                    f(out)
                    for out in output
                    for f in (lambda x: x + c.lower(), lambda x: x + c.upper())
                ]
        return output