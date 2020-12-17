# REVISIT THIS, seems like ther could be a better answer
"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

 
"""
class Solution:
    def nextClosestTime(self, time: str) -> str:
        """
        step 1: look at the digits and then sort them
        go from right to left, after making changes, go to right from that point
        
        HH cannot be greater than 24, and MM cannot be greater than 59
        
        MM seperate from HH
        
        if I can increase MM, then dont touch the HH 
        else make the MM minimum 
        
        09.59 ????
        """
        digits = []
        for i in [0, 1, 3, 4]:
            if time[i] not in digits:
                digits.append(time[i])
        digits.sort()
        minDigit = digits[0]
        
        if digits.index(time[4]) < len(digits) - 1:
            replacement = digits[digits.index(time[4]) + 1]
            if int(time[3] + replacement) <= 59:
                return time[0:4] + replacement
    
        if digits.index(time[3]) < len(digits) - 1:
            replacement = digits[digits.index(time[3]) + 1]
            if int(replacement + minDigit) <= 59:
                return time[0:3] + replacement + minDigit

        if digits.index(time[1]) < len(digits) - 1:
            replacement = digits[digits.index(time[1]) + 1]
            if int(time[0] + replacement) <= 23:
                return time[0] + replacement + ":" + (minDigit * 2)
    
        if digits.index(time[0]) < len(digits) - 1:
            replacement = digits[digits.index(time[0]) + 1]
            if int(replacement + minDigit) <= 23:
                return replacement + minDigit + ":" + (2 * minDigit)
        
        return (minDigit) * 2 + ":" + (minDigit * 2)

        