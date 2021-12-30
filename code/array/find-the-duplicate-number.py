from typing import List


class Solution:
    # Because the size of the array is n+1 and the numbers
    # in the array are in the range [1, n], each number will
    # represent an index that exists in the array.

    # Therefore, we can treat the array as a linked list with a cycle.
    # The starting point of the cycle is the duplicate number.

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        # find the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # find the starting point of the cycle
        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return start