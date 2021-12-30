from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [-1] * len(prices)

        def dfs(i=0):
            max_profit = 0

            if i >= len(prices):
                return 0

            if dp[i] != -1:
                return dp[i]

            # simulate buy at [i] and sell at [j]
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    max_profit = max(max_profit, prices[j] - prices[i] + dfs(j + 2))
                    dp[i] = max_profit

            # simulate cooldown at [i]
            max_profit = max(max_profit, dfs(i + 1))
            dp[i] = max_profit
            return max_profit

        return dfs()