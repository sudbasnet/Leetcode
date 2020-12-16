'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

 '''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        I just need to take care of the carry
        so I loop from the end to the beginning
        and just pass the carry on to the previous element in the array
        """
        carry = 1
        for i in reversed(range(len(digits))):
            val = digits[i] + carry
            if val >= 10:
                digits[i] = val % 10
                carry = 1
            else:
                digits[i] = val
                carry = 0

        if carry == 1:
            return [1] + digits
        return digits
        