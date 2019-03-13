# 1. Two Sum
# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.


# Implementation :
# We use One pass Hashmap to solve this problem. firstly before each
# add item into the dictionary, we will check if the complement value
# already exist in the dict, if yes, return the index of the complement
# and current index; if no, then add the item into the dictionray  
class Solution:
    def twoSum(self, nums ,target):
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                index = dic[complement]
                return [index, i]
            else:
                dic[nums[i]] = i
