"""
LeetCode Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/description/?language=Python


Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        self.longest = "" 
        
        for i in range(len(s)):
            self.expandir(s, i, i)
            
            self.expandir(s, i, i + 1)
            
        return self.longest
    
    def expandir(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            
            if current_len > len(self.longest):
                self.longest = s[left : right + 1]
            
            left -= 1
            right += 1

if __name__ == '__main__':
    sol = Solution()
    print(f"Resultado 1: {sol.longestPalindrome('babad')}")
    print(f"Resultado 2: {sol.longestPalindrome('cbbd')}")
    print(f"Resultado 2: {sol.longestPalindrome('neuquen')}")
    print(f"Resultado 2: {sol.longestPalindrome('123890098123123890098321')}")