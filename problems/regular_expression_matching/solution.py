"""
LeetCode Problem: Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching/description/?language=Python

Given an input string s and a pattern p, 
implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 
'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', 
there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            ignore_star = self.isMatch(s, p[2:])
            
            use_star = first_match and self.isMatch(s[1:], p)
            
            return ignore_star or use_star
            
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch('hola','hola'))
    print(sol.isMatch('aa','a*'))
    print(sol.isMatch('Hola','Hol.'))
    print(sol.isMatch('a*b*b','aab'))
    print(sol.isMatch('holanda','.*'))
    print(sol.isMatch('oso','OSO'))
    print(sol.isMatch('',''))
