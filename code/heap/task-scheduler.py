from typing import List
from collections import Counter
from heapq import heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the idea is to implement greedy algorithm by selecting tasks from maxHeap.
        res, heap, tasks = 0, [], Counter(tasks)

        for count in tasks.values():
            heappush(heap, -count)

        # we can use a time counter (i) to handle cooldown problem
        # under (i <= n), we can only select a specific task (e.g. "A") once
        while heap:
            i, done = 0, []
            while i <= n:
                i, res = i + 1, res + 1
                if heap:
                    count = -heappop(heap) - 1
                    if count != 0:
                        done.append(count)

                if not done:
                    break

            for count in done:
                heappush(heap, -count)

        return res