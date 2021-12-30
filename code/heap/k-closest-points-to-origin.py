from typing import List
import heapq


class Solution:
    # minheap1  O(klogn)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0] ** 2 + p[1] ** 2, *p) for p in points]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1:] for _ in range(k)]

    # minheap2  O(nlogk)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda p: p[0] ** 2 + p[1] ** 2)

    # sorted  O(nlogn)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
