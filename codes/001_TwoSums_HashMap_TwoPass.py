#1. Two Sum

# Given an array of integers, return indices of the two numbers
#  such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.


# This problem will be implemented using Hash map, 
# first after the analysis of the question, 
# there is only one solution, means there are no duplicates element in the list; 
# secondly, there are only one paar of elements which sum to the target.
class Solution:
    def twoSum(self, nums, target) :
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic.keys() and dic[complement] != i:
                return [i, dic[complement]]

# Issue:
# 1. The first time I have change the value of target, 
# which is quite improper, because if I have changed the value
# of target, at the next iteration, the compare of target with 
# the list element is changing. means the target is not the 
# original value. So a new variable muss be needed. 