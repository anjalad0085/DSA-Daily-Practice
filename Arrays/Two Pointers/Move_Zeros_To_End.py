class Solution:
    def pushZerosToEnd(self, arr):
        # j points to the index where the next non-zero element should be placed
        j = 0
        
        # Traverse the array
        for i in range(len(arr)):
            # If the current element is non-zero
            if arr[i] != 0:
                # Swap current element with element at index j
                arr[i], arr[j] = arr[j], arr[i]
                # Move j forward
                j += 1
        
        # Return the modified array
        return arr
