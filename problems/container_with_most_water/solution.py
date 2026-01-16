"""
LeetCode Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def max_area(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            
            current_area = current_width * current_height
            max_water = max(max_water, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.max_area([1,8,6,2,5,4,8,3,7]))
