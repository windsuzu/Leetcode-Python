from typing import List
import heapq


class Solution:
    # using sorted
    # time O(nlogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, key=lambda x: -x)[k - 1]

    # using maxheap
    # time O(n + klogn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        return [heapq._heappop_max(nums) for _ in range(k)][-1]

    # using quick_select
    # time O(n) avg. O(n^2) worse
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p < len(nums) - k:
                return quickSelect(p + 1, r)
            elif p > len(nums) - k:
                return quickSelect(l, p - 1)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)