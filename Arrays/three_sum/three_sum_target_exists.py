# Problem: Triplet Sum (Boolean)
# Given an integer array and a target value,
# check whether there exists a triplet whose sum equals the target.
#
# Approach:
# 1. Sort the array.
# 2. Fix one element and apply two pointers on the remaining array.
# 3. Move pointers based on comparison with target.
# 4. Skip duplicates to avoid redundant checks.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                s = arr[i] + arr[l] + arr[r]

                if s == target:
                    return True
                elif s > target:
                    r -= 1
                else:
                    l += 1

        return False
