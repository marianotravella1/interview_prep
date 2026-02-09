"""
LeetCode Problem: Palindrome Number
Link: [Pegar link aquí]
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        output = False

        if str(x) == str(x)[::-1]:
            output = True
        
        return output

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(123))
    print(sol.isPalindrome(12321))
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(12))
    print(sol.isPalindrome(-2))
    print(sol.isPalindrome(774474474477))
    