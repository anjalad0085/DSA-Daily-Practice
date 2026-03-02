# Problem: First Negative Integer in Every Window of Size K
# Given an array and an integer k, find the first negative
# integer in every contiguous subarray (window) of size k.
# If a window does not contain a negative integer, output 0.
#
# Category: Queue
# Technique: Sliding Window + Deque
#
# Approach:
# - Use a deque to store indices of negative elements.
# - Remove indices that fall out of the current window.
# - The front of the deque always represents the first negative element
#   in the current window.
#
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):
            # Remove elements outside the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Add current element if it is negative
            if arr[i] < 0:
                dq.append(i)

            # Window is ready
            if i >= k - 1:
                if dq:
                    result.append(arr[dq[0]])
                else:
                    result.append(0)

        return result
