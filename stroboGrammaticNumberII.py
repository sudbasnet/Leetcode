"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

exaple: input = 2, output = ["11","69","88","96"]
"""

"""
so its obviously a recursive problem. Or at least I see it that way. Once thing you can see is, you need to know what the reverse of each number is.
and only store the ones that are reversible. so 6 -> 9 and 9 -> 6, others are 0, 8 and 1.

the best way would be to divide the number into two parts left and right.
if you add something at the start of left, you need to add the reverse of the same thing at the end of right.
as long as the numbers are less than n. Since we need to add two things at once, our loop will have a for loop on n//2

if n is odd, at the end, we need to insert either an 8, 0 or 1 in the middle of left and right.
if n is even, we can simply combine left and right and return it.

"""
class Solution:
    def findStrobogrammatic(self, n: int) -> [str]:
        reversible = {'1':'1', '0':'0', '8':'8', '6':'9', '9':'6'}
        
        def getResults(addN, left, right):
            if addN == 0 and len(left) + len(right) == n:
                return [left+right]
            elif addN == 0:
                return [left+'1'+right, left+'8'+right, left+'0'+right]
            
            results = []
            for num, reverse in reversible.items():
                if not (left == '' and num == '0' and n > 1):
                    results += getResults(addN - 1, left+num, reverse+right)
            return results
        
        return getResults(n//2, "", "")
            