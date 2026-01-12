"""
LeetCode Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/description/?language=Python

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
 

Constraints:
-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        
        num_str = str(x)
        
        if num_str[0] == '-':
            num_rev = int(num_str[:0:-1])*-1
        else:
            num_rev = int(num_str[::-1])
        
        if -2**31 >= num_rev or num_rev >= 2**31 - 1:
            num_rev = 0
        
        return(num_rev)            
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-1123))
    print(sol.reverse(120))
