from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                # There is an overlap, merge them
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        
        return merged
    
ans=Solution()
print(ans.merge([[1,3],[2,6],[8,10],[15,18]]))
print(ans.merge([[1,4],[4,5]]))
                