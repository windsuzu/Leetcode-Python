from typing import List
from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # the idea is to expand the search from top-left to bottom-right
        # each time we pop the smallest element from the heap
        # and search its right and down by adding them to the heap
        seen = set()
        minHeap = [(matrix[0][0], 0, 0)]
        step = 1

        while step != k:
            val, i, j = heappop(minHeap)
            step += 1

            right = (matrix[i][j + 1], i, j + 1) if j + 1 < len(matrix[0]) else None
            down = (matrix[i + 1][j], i + 1, j) if i + 1 < len(matrix) else None

            if right and right not in seen:
                heappush(minHeap, right)
                seen.add(right)

            if down and down not in seen:
                heappush(minHeap, down)
                seen.add(down)

        return heappop(minHeap)[0]