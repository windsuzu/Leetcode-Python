from typing import List
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # store pair as (sum, index_nums1, index_nums2)
        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        seen = set()
        res = []

        while minHeap and len(res) != k:
            s, i, j = heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            cand1 = (nums1[i + 1] + nums2[j], i + 1, j) if i + 1 < len(nums1) else None
            cand2 = (nums1[i] + nums2[j + 1], i, j + 1) if j + 1 < len(nums2) else None

            if cand1 and cand1 not in seen:
                seen.add(cand1)
                heappush(minHeap, cand1)

            if cand2 and cand2 not in seen:
                seen.add(cand2)
                heappush(minHeap, cand2)

        return res