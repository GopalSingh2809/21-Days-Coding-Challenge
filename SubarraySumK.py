from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        # Use a hash table (dictionary) to store the frequency of prefix sums
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1  # Initialize with prefix sum 0 occurring once

        for num in nums:
            prefix_sum += num  # Update the prefix sum
            # If (prefix_sum - k) exists in the hash table, add its frequency to count
            if (prefix_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - k]
            # Update the frequency of the current prefix sum in the hash table
            prefix_sum_counts[prefix_sum] += 1

        return count
    
ans=Solution()
print(ans.subarraySum([1,1,1], 2))  # Output:2