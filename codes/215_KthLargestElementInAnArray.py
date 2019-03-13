# Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. 
# Note that it is the kth largest element in the sorted order, 
# not the kth distinct element.

# Note : You may assume k is always valid, 1 ≤ k ≤ array's length.

# Implementation : sorted the array and find the last k-th element
# Actually this problem should be solved using heap.

import heapq
class Solution:
    def findKthLargest(self, nums,  k) :
        heapq.heapify(nums)
        while len(nums) != 0:

            if len(nums) == k:
                return heapq.heappop(nums)
            else:
                heapq.heappop(nums)
