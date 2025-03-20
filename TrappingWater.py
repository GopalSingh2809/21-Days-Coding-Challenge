class Solution:
    def trap(self,height: list[int]) -> int:
        if not height:
            return 0
    
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                print("left_max",left_max)
                water_trapped += max(0, left_max - height[left])
                print("Water Trapped : ",water_trapped)
            else:
                right -= 1
                right_max = max(right_max, height[right])
                print("Right_Max",right_max)
                water_trapped += max(0, right_max - height[right])
                print("Water Trapped : ",water_trapped)
        
        return water_trapped
    
ans=Solution()
length=int(input("Enter a number : "))
height=[]
print("Enter height bars : ")
for i in range(length):
    ele=int(input())
    height.append(ele)
    
print(ans.trap(height))