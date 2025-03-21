class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
         # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Half of the total elements
        
        # Binary search on the smaller array (nums1)
        left, right = 0, m
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2
            partition2 = half - partition1
            
            # Get the max and min elements around the partitions
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if the partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If the total number of elements is even
                if total % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # Move the partition to the left
                right = partition1 - 1
            else:
                # Move the partition to the right
                left = partition1 + 1
        
        raise ValueError("Input arrays are not sorted or invalid input.")
    
    
nums1,nums2=[],[]

len1=int(input("Enter the length of first array : "))
len2=int(input("Enter the length of second array : "))

print("Enter elements of first array :")
for i in range(len1):
    ele=int(input())
    nums1.append(ele)
    
print("Elements of second array :")
for i in range(len2):
    ele=int(input())
    nums2.append(ele)
    
res=Solution()
print("Median of the merged array is : ",res.findMedianSortedArrays(nums1,nums2))
    
