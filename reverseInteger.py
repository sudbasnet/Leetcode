"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


every round it increases by num * 10 + (x % 10) <= maxSize
num <= (maxSize - (x%10))//10

so if num > (maxSize - x%10)//10 then return 0
"""

def reverse(x):
    reversedNum = 0
    maxSize = (2**31) - 1
    multiplyBy = 1
    if x < 0:
        multiplyBy = -1
        x = -1 * x
    
    while x > 0:
        if reversedNum > (maxSize - (x%10))//10:
            return 0
        reversedNum = (reversedNum * 10) + (x % 10)
        x = x//10

    return reversedNum * multiplyBy