# Problem: Three Sum
# Given an integer array, return all unique triplets
# such that their sum is equal to 0.
#
# Approach:
# 1. Sort the array to easily handle duplicates and use two pointers.
# 2. Fix one element at a time and reduce the problem to Two Sum.
# 3. Use two pointers (left and right) to find pairs for the remaining sum.
# 4. Skip duplicate elements to avoid repeating triplets.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding output list)

class Solution:
    def triplets(self, arr):
        arr.sort()
        lst = []

        for i in range(len(arr) - 2):
            # Skip duplicate first elements
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            l = i + 1
            r = len(arr) - 1

            while l < r:
                s = arr[i] + arr[l] + arr[r]

                if s == 0:
                    lst.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates for left pointer
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1

                    # Skip duplicates for right pointer
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1

                elif s > 0:
                    r -= 1
                else:
                    l += 1

        return lst
