# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function 
# returns 0 when the reversed integer overflows.

# Check the input and output, if overflows return 0.
class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2 ** 31 - 1:
            return 0
        else:
            ans = ""
            nums = list(map(str, str(x)))
            if nums[0] == "-":
                numsNew = nums[1:]
                numsNew.reverse()
                ans = int(nums[0] + "".join(numsNew))
                if ans < -2**31 or ans > 2 ** 31 - 1:
                    return 0
                else:
                    return ans
            else:
                nums.reverse()
                ans = int("".join(nums))
                if ans < -2**31 or ans > 2 ** 31 - 1:
                    return 0
                else:
                    return ans
