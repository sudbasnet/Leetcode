class Solution:
    def climbStairs(self, n: int) -> int:
        """
        there are one way to get from stair01  to stair02
        there is one more way to get from stair00 to stair02 directly
        so if we only had stair00, stair01, stair02 (n = 2)
        there are two ways to get there, 
        stair00 --> stair02
        or stair00 -> stair01 -> stair02
        """
#        # works but time limit exceeds
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

        # we just need to know the numberOfWays for the last two steps
        # so we dont really need to create a whole array
        numberOfWays = []
            
        for i in range(n + 1):
            if i <= 2:
                numberOfWays.append(i)
            else:
                steps1 = numberOfWays[i-1]
                steps2 = numberOfWays[i-2]
                numberOfWays.append(steps1 + steps2)
        # print(numberOfWays)
        return numberOfWays[-1]
    
    """
    every way to get to i - 1 includes every way to get to the previous step
    """