class Solution:
    def increasingTriplet(self, nums) -> bool:
        '''
        we need to check if there are three numbers in increasing order.
        And we need to do it in linear runtime and O(1) space.
        
        ok so my initial approach was just a little off. See once you find 
        the first and second element, you just need to find soething
        that is greater than the second element. If we find something even
        smaller then we need to update the first and the second element.
        
        '''
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False