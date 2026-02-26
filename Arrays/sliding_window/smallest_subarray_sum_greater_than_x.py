# Problem: Smallest Subarray with Sum Greater Than X
# Given an array and an integer X, find the length of the
# smallest contiguous subarray with sum > X.
#
# Approach:
# - Use sliding window with two pointers.
# - Expand the window by moving right.
# - Shrink from the left while sum > X.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def smallestSubWithSum(self, x, arr):
        left = 0
        subsum = 0
        min_len = float('inf')

        for right in range(len(arr)):
            subsum += arr[right]

            while subsum > x:
                min_len = min(min_len, right - left + 1)
                subsum -= arr[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
