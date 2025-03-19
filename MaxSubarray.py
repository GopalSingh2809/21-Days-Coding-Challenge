class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        maxSum = nums[0]  # Initialize `maxSum` to the first element
        currentSum = nums[0]  # Initialize `currentSum` to the first element

        for num in nums[1:]:
            # Decide whether to start a new subarray or continue the current one
            currentSum = max(num, currentSum + num)
            # Update `maxSum` if `currentSum` is greater
            maxSum = max(maxSum, currentSum)

        return maxSum
    
res=Solution()
inputArray=[]
length=int(input("Enter the length : "))
print("Enter elements : ")
for i in range(length):
    ele=int(input())
    inputArray.append(ele)
    
print(res.maxSubArray(inputArray))
    