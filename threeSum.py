class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        the best solution I can see is a n^2 solution. Sometimes those are not so bad
        
        it is the same concept as the 2Sum problem. in this case we first store the values and indices
        in a dictionary. then we do a double for loop and check is target - (sum of two numbers) is in the 
        dictionary. If it is then return the actual numbers.
        
        since it says triplets, we need to start for loop index i at 0, another at i+1 to end and only
        look at indices in the dictionary from that point onwards
        
        note that there could be duplicates so we need to save all the indices that a certain number is seen
        """
        results = []
            
        seenNums = {}
        for i in range(len(nums)):
            seenNums[nums[i]] = seenNums.get(nums[i], 0) + 1
        
        print("seenNums: ", seenNums)
        newNums = []
        newSeenNums = {}
        for num, repeats in seenNums.items():
            if num == 0 and repeats >= 3:
                results.append([0, 0, 0])
            if num!= 0 and repeats > 1 and -(num+num) in seenNums:
                results.append([num, num, -(num+num)])
            newSeenNums[num] = len(newNums)
            newNums.append(num)
        
        for i in range(len(newNums)-2):
            for j in range(i+1, len(newNums)-1):
                target = -(newNums[i]+newNums[j])
                if target in newSeenNums and newSeenNums[target] > j:
                    results.append([newNums[i], newNums[j], target])
                    
        return results
        """
        OK!!! this took a while!!!
        first I stored everything in a dictionary with the number of repeatations of each character. 
        now if 0 is repeated 3 or more times, we know there should be a [0, 0, 0], we add that
        if a number id repeated more than once, we look for -(num+num) in dictionary, if exists, add the combo
        finally, we create a new nums list with all unique characters.
        now, we go through the new list one more time to store the location of each number
        now we are ready to do the double for loop and search for the third element
        """
        
                      