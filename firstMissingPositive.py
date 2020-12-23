class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        I looked at the solution. Couldn't figure out myself.
        The idea is:
        If the array of sze k had nothing missing, you would have [1, ... , 1 + k]
        
        So first of all, you make all the values lower than 0 to 0.
        then you need to see id a number has occured in the list. 
        You would need something like a hash, but we need to use constant space.
        Since we know the values should be between 1 ... 1 + k, we can use the index 
        of the array as the hash. 
        
        But now we need a way to retrieve the original value present in the list
        along side the number of times the number associated with the array has been
        seen.
        
        nums[ nums[i]%n ] += n    # n is length of array
        think about it!!
        nums[i] is the current number we are looking at, which is in a for loop
        #   how can we store the number of times we have seen the number denoted by i?? 
        #   and what is the original number in the array??
        
        note that 1%n (if n is > 1) is 1, similarly if n = 4, 1%4, 2%4, 3%4 all equal to 
        their own value, also note that any multiple of n modulo n (2n % n) is zero.
        
        so what's hapenning is, if I see a 2 at index 0, I go to the index 2 and add the value 
        n to it. So now if I modulo the number at index 2, I get the original value at index 2.
        And if I divide the value (//) I get the number of times the number 2 has been seen 
        in the array.
        
        '''
        nums.append(0) # hashing must start from 0
        n = len(nums)
        
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n: 
                nums[i] = 0
                
        for i in range(len(nums)):
            nums[ nums[i]%n ] += n
        
        for i in range(1, len(nums)):
            if nums[i]//n == 0:
                return i

        return n
