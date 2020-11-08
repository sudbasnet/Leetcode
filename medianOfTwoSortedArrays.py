class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        I have solved this problem at some point, so I have the general idea of how to do it.
        
        The idea is simple, to find the median of the combo of the sorted arrays, I just need to 
        know how many of the elements of the first array is on the left of the median. I dont 
        need to sort everything out.
        
        Here's an example:
        1 4 6 8 9   : array 1
         2 5 7   10 : array 2
        
        9 total elements
        means there must be 4 elements on each side and one median
        
        point is, we know there must be 4 total elements on the left.
        Lets start with the assumption that there are 2 elements of the first array
        and 2 elements of the second array in the left of the combined array.
        
        left | right
        -----|------
         1 4 | 6 8 9
         2 5 | 7 10
         
         the condition to check the validity is:
         max(left of array1, left of array2) < min(right of array1, right of array2)
         
         otherwise we move things around until its true.
         return the min of the right portion of array1 and array2.
        """
        combinedLength = len(nums1) + len(nums2)
        itemsOnLeft = combinedLength // 2
        
        # indices of the breaking point of nums1 and nums2 arrays
        # the indices are on the left side of the partition
        nums1LeftEnd = len(nums1[:itemsOnLeft//2]) - 1
        nums2LeftEnd = itemsOnLeft - len(nums1[:itemsOnLeft//2]) - 1

        # helper functions so I dont need to handle overflow
        def nums1At(index):
            if index < 0:
                return float("-inf")
            elif index > len(nums1) - 1:
                return float("inf")
            return nums1[index]

        def nums2At(index):
            if index < 0:
                return float("-inf")
            elif index > len(nums2) - 1:
                return float("inf")
            return nums2[index]

        while max(nums1At(nums1LeftEnd), nums2At(nums2LeftEnd)) > min(nums1At(nums1LeftEnd + 1), nums2At(nums2LeftEnd + 1)):
            if nums1At(nums1LeftEnd) > nums2At(nums2LeftEnd + 1):
                nums1LeftEnd -= 1
                nums2LeftEnd += 1
            elif nums2At(nums2LeftEnd) > nums1At(nums1LeftEnd + 1):
                nums2LeftEnd -= 1
                nums1LeftEnd += 1

        if combinedLength % 2 == 0:
            return (max(nums1At(nums1LeftEnd), nums2At(nums2LeftEnd)) + min(nums1At(nums1LeftEnd + 1), nums2At(nums2LeftEnd + 1)))/2
        else:
            return min(nums1At(nums1LeftEnd + 1), nums2At(nums2LeftEnd + 1))