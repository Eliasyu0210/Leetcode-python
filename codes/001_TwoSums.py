#  Given an array of integers, return indices of the two numbers
#  such that they add up to a specific target.

#  You may assume that each input would have exactly one solution, 
#  and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]

# ISSUES:
# 1. 
