"""
LeetCode Problem 35. Search Insert Position
Link: [Paste link here]
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Return the index if the target is found. If not, return the index where it would be inserted in order."""
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
    print(sol.searchInsert([1, 3, 5, 6], 0))  # 0
