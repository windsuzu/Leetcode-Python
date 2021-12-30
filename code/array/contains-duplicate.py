# You can just compare the length of list and set 😀

class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))