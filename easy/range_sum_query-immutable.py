from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.csum = []
        c = 0
        for num in nums:
            c+=num
            self.csum.append(c)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.csum[right]
        
        return self.csum[right] - self.csum[left-1] 


nums = [-2, 0, 3, -5, 2, -1]

# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)

print(obj.sumRange(0, 2))
print(obj.sumRange(1, 4))
print(obj.sumRange(2, 5))