"""
LeetCode Problem: Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/?language=Python

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index: int, current_str: str):
            if len(current_str) == len(digits):
                result.append(current_str)
                return

            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            for letter in possible_letters:
                backtrack(index + 1, current_str + letter)

        backtrack(0, "")

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("7886"))
    print(sol.letterCombinations("35"))
    print(sol.letterCombinations("783"))
    print(sol.letterCombinations("533"))
    print(sol.letterCombinations("5252"))
