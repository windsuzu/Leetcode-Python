from typing import List
from collections import deque


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # the idea is to use two pointers (l, r)
        # to narrow the range (l - r) so that it's equal to k
        # the time complexity is O(n)
        l, r = 0, len(arr) - 1

        while (r - l) >= k:
            if x - arr[l] > arr[r] - x:
                l += 1
            else:
                r -= 1

        return arr[l : r + 1]

    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        # or use a deque to implement the method like two pointers
        q = deque(arr)
        while len(q) > k:
            q.popleft() if x - q[0] > q[-1] - x else q.pop()
        return q