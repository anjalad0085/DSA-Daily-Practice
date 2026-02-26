# Problem: Two Sum (Boolean version)
# Given an array and a target, check if there exists
# a pair of elements whose sum equals the target.
#
# Approach:
# - Use a hashmap (dictionary) to store elements seen so far.
# - For each element, compute the required complement (target - current element).
# - If the complement already exists in the hashmap, return True.
# - Otherwise, store the current element in the hashmap.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, arr, target):
        d = {}
        for i in range(len(arr)):
            a = target - arr[i]
            if a in d:
                return True
            d[arr[i]] = i
        return False
