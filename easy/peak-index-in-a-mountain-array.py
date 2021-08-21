from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr)-1
        
        while True:
            mid = (low + high) // 2
            
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1]:
                high = mid-1
            elif arr[mid] < arr[mid+1]:
                low = mid+1