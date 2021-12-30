from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        max_dp = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # find a possible subseq
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        cnt[i] = cnt[j]

                    elif dp[i] == 1 + dp[j]:
                        cnt[i] += cnt[j]

            max_dp = max(dp[i], max_dp)

        return sum([cnt[i] for i in range(len(nums)) if dp[i] == max_dp])