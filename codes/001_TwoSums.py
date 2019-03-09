#  Given an array of integers, return indices of the two numbers
#  such that they add up to a specific target.

#  You may assume that each input would have exactly one solution, 
#  and you may not use the same element twice.


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        dic = list(enumerate(nums))
        for i in range(len(dic)):
            for j in range(len(dic)):
                if dic[i][1] == target - dic[j][1]:
                    if dic[i][0] != dic[j][0]:
                        return [i, j]

# ISSUES:
# 1. 
