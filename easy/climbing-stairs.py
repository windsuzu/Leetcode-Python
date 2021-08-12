class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        history = [1, 2]
        for i in range(2, n):
            total = history[i-1] + history[i-2]
            history.append(total)
            
        return history[-1]
