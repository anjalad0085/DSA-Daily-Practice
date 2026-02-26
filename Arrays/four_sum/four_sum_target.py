# Problem: Four Sum (Return all unique quadruplets)
# Given an integer array and a target value,
# return all unique quadruplets [a, b, c, d]
# such that a + b + c + d == target.
#
# Approach:
# 1. Sort the array.
# 2. Fix first two elements using two loops.
# 3. Use two pointers (left, right) for remaining part.
# 4. Skip duplicates to avoid repeating quadruplets.
#
# Time Complexity: O(n^3)
# Space Complexity: O(1) (excluding output list)

class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        res = []
        n = len(arr)

        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                l = j + 1
                r = n - 1

                while l < r:
                    s = arr[i] + arr[j] + arr[l] + arr[r]

                    if s == target:
                        res.append([arr[i], arr[j], arr[l], arr[r]])
                        l += 1
                        r -= 1

                        while l < r and arr[l] == arr[l - 1]:
                            l += 1
                        while l < r and arr[r] == arr[r + 1]:
                            r -= 1

                    elif s > target:
                        r -= 1
                    else:
                        l += 1

        return res
