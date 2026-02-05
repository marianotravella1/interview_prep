"""
LeetCode Problem: 30. Substring with Concatenation of All Words
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""


from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)

        word_len = len(words[0])
        window_len = len(words) * word_len
        res = []

        for i in range(len(s) - window_len + 1):
            def findSubstring(self, s: str, words: List[str]) -> List[int]:
                if not words or not s:
                    return []

        w = len(words[0])
        n = len(words)
        need = Counter(words)
        res = []

        for start in range(w):
            left = start
            seen = Counter()
            count = 0

            for right in range(start, len(s) - w + 1, w):
                word = s[right: right+w]

                if word not in need: # variables reset logic
                    seen.clear()
                    count = 0
                    left = right + w
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > need[word]:
                    left_word = s[left: left+w]
                    seen[left_word] -= 1
                    count -= 1
                    left += w

                if count == n:
                    res.append(left)

        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubstring('barfoofoobarthefoobarman', ["bar","foo","the"]))
    
