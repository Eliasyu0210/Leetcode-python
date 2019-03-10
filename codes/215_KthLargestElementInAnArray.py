# Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Note : You may assume k is always valid, 1 ≤ k ≤ array's length.

# Implementation : sorted the array and find the last k-th element
# Actually this problem should be solved using heap.

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[-k]
