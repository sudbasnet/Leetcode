class Solution:
    def maxProduct(self, nums: [int]) -> int:
        """
        its a little tricky, we use the same logic as used in maxSum problem,
        in maxSum we just record the maxSum so far as we move in the array
        here, since multiplying by negative at any point could change the maximum
        we should record the maximum so far, as well as minimum so far.
        
        so we need to find the product not the actual subarray
        
        again, how do we know that we need to break at a point and start a new array??
        
        1 2 3 0 3
        1 2 6 0 3
        break ^
        
        but its more complicated in products, because there could be negative numbers
        
        so if a new product is less than the max, break the max so the runningProduct changes??
        when we see a 0, we break. Because it doesnt matter what is before a 0, a product with 0 makes
        everything 0
        
        so everytime we see a 0, we break. 
        otherwise the only reason to break would be if the final product is -ve, in which case we should 
        break before the last -ve integer or after the first -ve integer
        
        here's another method I tried but didnt work properly. 
        divide the input into various lists based on any zeros present. 
        Then check the max product in each list. compare them at the end and return the max
    
        New Plan:
        --------
        have a runningProduct and a productAfterFirstNegative 
        runningProduct just multiplies everything it sees.
        productAfterFirstNegative multiplies everything after the first negative number is seen
        0 resets everything
        maxProduct keeps track of the max product seen so far throughout the program
        """
        if not nums:
            return 0
        
        # holds max product seen so far
        maxProduct = float("-inf")
        runningProduct = 1 # will keep multiplying until we see a 0
        productAfterFirstNeg = 1
        seenNegative = False
        
        for i in range(len(nums)):
            if nums[i] == 0:
                maxProduct = max(maxProduct, 0)
                runningProduct = 1
                productAfterFirstNeg = 1
                seenNegative = False
            else:
                # multiply everything you see
                runningProduct *= nums[i]

                # check if negative is seen already,
                # multiply if already seen, else start multiplying from next round
                if not seenNegative and nums[i] < 0:
                    seenNegative = True
                    productAfterFirstNeg = 1
                    maxProduct = max(maxProduct, runningProduct)
                else:
                    productAfterFirstNeg *= nums[i]
                    maxProduct = max(maxProduct, runningProduct, productAfterFirstNeg)
        
        return maxProduct
