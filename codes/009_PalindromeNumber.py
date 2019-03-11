# 9. Palindrome Number
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Follow up:
# Coud you solve it without converting the integer to a string?

# Implementation: if the input is negative ,the palindrom number will 
# put the "-" at the end of number, which means not the same as
# original number.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            digits = []
            while x != 0:
                digit = int(x % 10)
                x = int(x / 10)
                digits.append(digit)
            newDigits = digits[::-1]
            return newDigits == digits
