"""
LeetCode Problem: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/?language=Python

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        idx = 0
        while idx < len(first) and idx < len(last):
            if first[idx] == last[idx]:
                idx += 1
            else:
                break
                
        return first[:idx]

if __name__ == "__main__":
    sol = Solution()
    
    print(f"Test 1: {sol.longestCommonPrefix(['flower', 'flow', 'flight'])}") 
    print(f"Test 2: {sol.longestCommonPrefix(['dog', 'racecar', 'car'])}")   
    print(f"Test 3: {sol.longestCommonPrefix(['interstellar', 'internet', 'interval'])}") 