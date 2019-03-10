# Given two arrays, write a function to compute their intersection.

# Basic implementation:
# In order to find out the duplicate element in the array,
# I can't just easily to check existance ofthe pop out value from the 
# first array in the second array.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        while len(nums1) != 0:
            a = nums1.pop()
            if a in nums2:
                ans.append(a)
                nums2.remove(a)
        ans.sort()
        return ans

