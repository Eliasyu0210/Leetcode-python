# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns 
# are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order,
# not the kth distinct element.

# Basic implemtation :
# Conveter the matrix to list and to heap,
#  then pop the first kth value and return the last
import heapq

class Solution:
    def kthSmallest(self, matrix, k) -> int:
        ans = []
        for row in matrix:
            ans += row
        heapq.heapify(ans)
        for i in range(k):
            a = heapq.heappop(ans)

        return a
