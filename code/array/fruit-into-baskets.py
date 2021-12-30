from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, count, res = 0, {}, 0

        for r, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1

            res = max(res, r - l + 1)
        return res