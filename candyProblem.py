class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        looks like we need to look at the values of the array around us.
        also the number of candies that the children at those places have received
        
        
        so find pits. Priorities where the left and right have priority larger than self
        assign one candy to the pits and 2 candies otherwise
        -- thats our starting point --- O(n)
        
        since pits can have just one candy ???
        
        we can look at the whole array from the point of view of the pits.
        
        And the peaks will have the max value derived as we go from pits to peaks
        '''
        '''
        NOw use the same concept and try to do it in two passes,
        in the first pass you go from left to right, only assign values where something
        is increasing as you go from left to right. And when you going from right to left, 
        only assign values where values increase right to left
        '''
        candies = [1 for _ in ratings]
        
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
        
        for j in reversed(range(1, len(ratings))):
            if ratings[j] < ratings[j-1]:
                if j == 1 or ratings[j-2] <= ratings[j-1]:
                    candies[j-1] = max(candies[j-1], candies[j] + 1)
                else:
                    candies[j-1] = candies[j] + 1
        
        return sum(candies)
            