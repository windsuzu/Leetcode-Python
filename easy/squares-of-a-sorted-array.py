from collections import deque
from typing import List


class Solution:
    # Method 1 - Two Pointers
    def sortedSquares_1(self, nums: List[int]) -> List[int]:
        nums = [num * num for num in nums]
        l = deque()

        a, b = 0, len(nums) - 1
        while a != b:
            if nums[a] >= nums[b]:
                l.appendleft(nums[a])
                a += 1
            else:
                l.appendleft(nums[b])
                b -= 1
        else:
            l.appendleft(nums[a])
        return l

    # Method 2 - Sorted
    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])
