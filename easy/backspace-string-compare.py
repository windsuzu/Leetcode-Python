class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sp, tp = len(s) - 1, len(t) - 1

        def back(string, pointer):
            count = 0
            while True:
                if string[pointer] == "#":
                    count += 1
                else:
                    count -= 1

                if count >= 0 and pointer >= -1:
                    pointer -= 1
                else:
                    break

            return pointer

        while True:
            sp = back(s, sp)
            tp = back(t, tp)

            if sp <= -1 and tp <= -1:
                return True
            if sp <= -1 and tp != -1:
                return False
            elif sp != -1 and tp <= -1:
                return False
            elif s[sp] != t[tp]:
                return False

            sp, tp = sp - 1, tp - 1