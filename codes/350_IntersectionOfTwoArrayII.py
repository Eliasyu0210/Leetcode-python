# Given two arrays, write a function to compute their intersection.

# Basic implementation 1:
# Using hash map first find out the number of each element in
# each array, and then the minimum value of element will be 
# added into the resultant list
import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Count = collections.Counter(nums1)
        num2Count = collections.Counter(nums2)
        ans = []
        for key in num1Count:
            if key in num2Count:
                if num1Count[key] >= num2Count[key]:
                    ans += num2Count[key] * [key]
                else:
                    ans += num1Count[key] * [key]
        return ans
