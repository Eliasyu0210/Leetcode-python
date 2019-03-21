#  Given a string, find the length of the longest substring
#  without repeating characters.

# Brute force solution. 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            subString = s[0]
            subStringLength = len(subString)
            for i in range(len(s)-1):
                for j in range(i+1, len(s)):
                    if s[j] in s[i: j]:
                        subString = s[i: j]
                        if subStringLength < len(subString):
                            subStringLength = len(subString)
                        break
                    else:
                        subString = s[i: j+1]
                        if subStringLength < len(subString):
                            subStringLength = len(subString)
            return subStringLength

# ISSUES:
# 1. In the first loop the cycles are length of the string minus 1
#    which means if the string length less than one, the munipulation
#    is missing. So, make the subString to the first charater of the
#    string.