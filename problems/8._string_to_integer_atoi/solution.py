"""
LeetCode Problem: String to Integer
Link: https://leetcode.com/problems/string-to-integer-atoi/?language=Python
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1 
            i += 1
            
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            

            result = result * 10 + digit
            i += 1
            

        result *= sign
        

        INT_MIN = -2**31       
        INT_MAX = 2**31 - 1    
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result

if __name__ == "__main__":
    solution = Solution()
    
    print(f"Test 1 '42': {solution.myAtoi('42')}")
    print(f"Test 2 '   -042': {solution.myAtoi('   -042')}")
    print(f"Test 3 '1337c0d3': {solution.myAtoi('1337c0d3')}")
    print(f"Test 4 '0-1': {solution.myAtoi('0-1')}")
    print(f"Test 5 'words and 987': {solution.myAtoi('words and 987')}")
    

    print(f"Overflow Test: {solution.myAtoi('-999999999999')}") 
        
        
        
