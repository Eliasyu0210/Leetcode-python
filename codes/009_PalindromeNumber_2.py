# 9. Palindrome Number
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Follow up:
# Coud you solve it without converting the integer to a string?

# Implementation: 
# 1.if the input is negative ,the palindrom number will 
# put the "-" at the end of number, which means not the same as
# original number.
# 2. The origin input value shouldn't be changed if we want to compare
# it with the new output, means I should give the "x" value to a new variable

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            digits = 0
            new = x
            while new != 0:
                digit = int(new % 10)
                new = int(new / 10)
                digits = digits * 10 + digit
            return x == digits


