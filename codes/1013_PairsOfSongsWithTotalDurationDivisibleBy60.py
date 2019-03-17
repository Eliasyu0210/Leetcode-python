# 1013. Pairs of Songs With Total Durations Divisible by 60

# In a list of songs, the i-th song has a duration of time[i] seconds.

#Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

# SHORT IMPLEMENTATION:
# This question is similar to the 001st question, which is the two sum question. The basic ideal was to calculate the remainder of each element,
# here a special situation must be concerned. Which is remainder equal to 0. In this situation, the item will will be added to the dictionary should be 60.
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        ans = 0
        dic = {}
        # One-pass
        for i in time:
            temp = i % 60

            complement = 60 - temp
            if complement in dic:
                ans += dic[complement]

            if temp != 0:
                if temp in dic:
                    dic[temp] += 1
                else:
                    dic[temp] = 1
            if temp == 0:
                if 60 in dic:
                    dic[60] += 1
                else:
                    dic[60] = 1
        return ans
