from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letter_set = {ord(l) for l in letters}
        target = ord(target) + 1
        
        while True:
            if target in letter_set:
                return chr(target)
            target = target + 1 if target < 122 else 97