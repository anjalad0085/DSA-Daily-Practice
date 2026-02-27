# Problem: K Sized Subarray Maximum
# Given an array and an integer k, find the maximum
# for each contiguous subarray of size k.
#
# Category: Queue
# Technique: Sliding Window + Monotonic Deque
#
# Approach:
# - Use a deque to store indices of elements.
# - Maintain the deque in decreasing order of values.
# - Remove indices that are out of the current window.
# - The front of the deque always stores the index of the maximum element.
#
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        dq = deque()
        result = []

        for i in range(len(arr)):
            # Remove elements outside the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (maintain decreasing order)
            while dq and arr[i] > arr[dq[-1]]:
                dq.pop()

            dq.append(i)

            # Add maximum for the current window
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
