from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # the idea is to use a (max_heap) and a temp variable (prev)

        # in each iteration
        # 1. we pop and append the most common character
        # 2. we push the previous popped character back into the heap
        #    if it exists and the counter is still greater than 0
        # 3. store the new popped character to (prev) with counter - 1

        res, c, heap = "", Counter(s), []

        for c, freq in c.items():
            heapq.heappush(heap, (-freq, c))

        prev = (0, "")
        while heap:
            freq, c = heapq.heappop(heap)
            res += c

            if prev[0] != 0:
                heapq.heappush(heap, prev)

            prev = (freq + 1, c)

        return res if len(res) == len(s) else ""