from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) <= len(s2):
            s1Count, s2Count = [0] * 26, [0] * 26

            for i in range(len(s1)):
                s1Count[ord(s1[i]) - ord("a")] += 1
                s2Count[ord(s2[i]) - ord("a")] += 1

            if self.check(s1Count, s2Count):
                return True

            for i in range(len(s1), len(s2)):
                s2Count[ord(s2[i - len(s1)]) - ord("a")] -= 1
                s2Count[ord(s2[i]) - ord("a")] += 1
                if self.check(s1Count, s2Count):
                    return True
        return False

    def check(self, s1Count: List[int], s2Count: List[int]) -> bool:
        return all([s1Count[i] == s2Count[i] for i in range(len(s1Count))])
