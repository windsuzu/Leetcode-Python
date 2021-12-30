class Solution:
    def climbStairs(self, n: int) -> int:
        # we can use dynamic programming
        # the last step = 1
        # the second-last step = 1, because we can only take 1 step to the last
        
        # start from the third-last step
        # we can take both 1 step or 2 steps
        # therefore, this is a Fibonacci sequence
        
        a, b = 1, 1
        for i in range(n-1):
            a, b = a+b, a
        return a