from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        index = 0
        n = len(heights)
        
        while index < n:
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                width = index if not stack else index - stack[-1] - 1
                area = heights[top_of_stack] * width
                max_area = max(max_area, area)
        
        while stack:
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top_of_stack] * width
            max_area = max(max_area, area)
        
        return max_area
    
    
ans=Solution()
print(ans.largestRectangleArea([2,1,5,6,2,3]))
print(ans.largestRectangleArea([2,4]))