from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
    
        n = len(nums)
        result = []
        dq = deque()
        
        for i in range(n):
            # Remove indices of elements not in the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices of all elements smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current element's index to the deque
            dq.append(i)
            
            # If the window has reached size k, add the maximum to the result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
ans=Solution()
print(ans.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)) # Output:[3,3,5,5,6,7]
print(ans.maxSlidingWindow([1],1)) # Output:[1]