from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        target = sum(nums) // k

        nums.sort(reverse=True)
        used = [False] * len(nums)

        def dfs(k, subsum=0, index=0):
            if k == 1:
                return True

            if subsum == target:
                return dfs(k - 1)

            for i in range(index, len(nums)):
                if not used[i] and subsum + nums[i] <= target:
                    used[i] = True
                    if dfs(k, subsum + nums[i], i + 1):
                        return True
                    used[i] = False
            return False

        return dfs(k)