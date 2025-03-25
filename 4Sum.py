from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early termination if the smallest sum is greater than target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Early termination if the largest sum is less than target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Early termination if the smallest sum is greater than target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Early termination if the largest sum is less than target
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result
    
ans=Solution()
print(ans.fourSum([1, 0, -1, 0, -2, 2],0))
print(ans.fourSum([2,2,2,2,2],8))