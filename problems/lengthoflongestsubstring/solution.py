"""
LeetCode Problem: length_of_longest_substring
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1878313181/?language=Python
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        # use enumerate instead of range for better readability
        for right, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(char)
            current_len = right - left + 1
            max_len = max(max_len, current_len)

        return max_len
    
if __name__ == "__main__":
    string = "abcabcbb"
    solution = Solution()
    result = solution.length_of_longest_substring(string)
    print(f"Longitud máxima: {result}")
    string = "bbbbb"
    result = solution.length_of_longest_substring(string)
    print(f"Longitud máxima: {result}")  
