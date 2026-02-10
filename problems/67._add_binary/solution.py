"""
LeetCode Problem: 67. Add Binary
Link: https://leetcode.com/problems/add-binary/description/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []

        idxA, idxB = len(a) - 1, len(b) - 1

        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1

            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("11", "1"))  # "100"
    print(sol.addBinary("1010", "1011"))  # "10101"
