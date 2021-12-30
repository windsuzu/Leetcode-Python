from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.csum = nums
        for i in range(1, len(nums)):
            self.csum[i] += self.csum[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.csum[right] - (self.csum[left-1] if left != 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)