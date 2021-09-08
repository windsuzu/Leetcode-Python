from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1, nums[0]]
        backward = [nums[-1]]
        
        for i, num in enumerate(nums[1:-1]):
            answer.append(num*answer[i+1])
        
        for i, num in enumerate(nums[-2::-1]):
            backward.append(num*backward[i])
            answer[-2-i] = backward[i] * answer[-2-i]
            
        return answer


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
