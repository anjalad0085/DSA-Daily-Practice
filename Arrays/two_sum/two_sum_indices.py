# Problem: Two Sum (Return Indices)
# Given an array of integers and a target value,
# return the indices of the two numbers such that
# they add up to the target.
#
# Approach:
# - Use a hashmap to store numbers and their indices.
# - For each element, compute the complement (target - current number).
# - If the complement exists in the hashmap, return both indices.
# - Otherwise, store the current number with its index.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            t = target - nums[i]

            if t in d:
                return [d[t], i]

            d[nums[i]] = i
