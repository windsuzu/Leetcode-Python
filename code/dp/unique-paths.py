class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # the idea is to use 2D matrix dynamic programming
        # from finish point back to start point
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # base case: the finish point will be "dp[m-1][n-1] = 1"
        dp[-1][-1] = 1
        
        # we can iterate through all the cells
        # the value of each cell will be the sum from the right and bottom cells
        # For example:
        # dp[1][6] = dp[1][7] + dp[2][6]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i + j == m + n - 2:
                    continue
                right = dp[i][j+1] if j+1 < n else 0
                bottom = dp[i+1][j] if i+1 < m else 0
                dp[i][j] = right + bottom
        
        return dp[0][0]