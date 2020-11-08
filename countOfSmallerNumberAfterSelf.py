class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        One solution that I thought of was:
            you go from right to left, and sort the array one element at a time
            * sort in descending order

            the new placement of any element in the array will tell it how many
            elements were smaller than itself on the right.

            It might not be too bad because, you can use the merge sort kind of 
            technique to divide and sort the array. Lets figure out the details
            
            # hint is: use the same technique as the merge sort
              [5,2, 6,1]
            [5, 2]  [6, 1]
            [5][2]  [6][1]
            
            [2, 5]  [1, 6]
            
            5 moved one place to the right,(1)
            6 moved one place to the right (1)
            2 moved one place to the left (0)
            1 moved one place to the left (0)
            
            [1, 2, 5, 6]
            
            1 moved further back (0)
            2 moved one to the right (1)
            5 moved one more to the right (2)
            6 remained in the last position (1)
            
            jumps to the right is what determines the number of elements on the right
            that are smaller than it self
            
            CODE:
            record the original index in the numbers
            numsIndex = [[nums[i], i] for i in range(len(nums))]
            write the sort and merge methods
        """                 
        indices = {}
        result = [0] * len(nums)
        
        numsWithIndex = []
        for i in range(len(nums)):
            numsWithIndex.append([nums[i], i])
            indices[i] = 0
        
        def divideIntoLists(numsList):
            if len(numsList) <= 1:
                return numsList
            mid = len(numsList)//2
            return mergeLists([divideIntoLists(numsList[:mid]), divideIntoLists(numsList[mid:])])
        
        
        def mergeLists(twoLists):
            [left, right] = twoLists
            sortedList = []
            rightCounter = 0
            while left or right:
                # if left and not right 
                # requires update
                if right and not left:
                    return sortedList + right
                elif left and not right:
                    indices[left[0][1]] += rightCounter
                    sortedList.append(left.pop(0)) 
                elif left[0][0] > right[0][0]:
                    rightCounter += 1
                    sortedList.append(right.pop(0))
                else:
                    indices[left[0][1]] += rightCounter
                    sortedList.append(left.pop(0))
            return sortedList
        
        divideIntoLists(numsWithIndex)
        return [indices[i] for i in range(len(nums))]
        
        
        