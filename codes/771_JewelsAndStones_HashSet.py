# 771. Jewels and Stones
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".


# Using Hashset, the string of jewels will be seted to a Hashset. which means the time complexity of each search will be O(1)

# in python using set for the usage of hashset, because the search in set() is also O(1)
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Jset = set(J)

        ans = 0
        for char in S:
            if char in Jset:
                ans += 1
        return ans
