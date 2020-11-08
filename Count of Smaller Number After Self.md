# Count of Smaller Numbers after self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

### Example:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

### Constraints:
```
0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
```
## Solution
This one took me a day and a half to figure out. So I thought I'd try to document it a little. It was not the most efficient solution, perhaps I can optimize it further, I might do that in the future. The key to the solution is the **Merge Sort** algorithm. [Here](https://www.youtube.com/watch?v=alJswNJ4P3U&t=1380s) is an excellent description of the merge sort algorithm by [Back To Back SWE](https://www.youtube.com/channel/UCmJz2DV1a3yfgrR7GqRtUUA). Back To Back SWE might be my favorite channel on YouTube when it comes to solving coding interview questions.

### Thought process
Here are a bunch of random points I went through:
*   you go from right to left, and sort the array one element at a time
*   sort in descending order
*   the new placement of any element in the array will tell it how many
elements were smaller than itself on the right.
*   It might not be too bad because, you can use the merge sort kind of 
technique to divide and sort the array. Lets figure out the details

**Looked Up a hint at this point**
* Hint was to use the same technique as the merge sort, so I was close.

* Breaking down the example
```
 [5,2, 6,1]
[5, 2]  [6, 1]
[5][2]  [6][1]

[2, 5]  [1, 6]

5 moved one place to the right,(1)
6 moved one place to the right (1)
2 moved one place to the left (-1)
1 moved one place to the left (-1)

then

1 moved further back (-1)
2 moved one to the right (1)
5 moved one more to the right (2)
6 remained in the last position (1)

CONCLUSION: 
jumps to the right is what determines the number of elements on the right
that are smaller than itself
```
### Code plan:
* record the original index in the numbers by creating a new array with both, the value and the index. eg [[5,0], [2,1], [6,2], [1,3]]
* write a method to divide the array into two halves
* write a method to merge two input arrays
    * input comes in as **left** and **right** arrays
    * if first element of **left** is larger than the first element of **right**, then everything on the left moves by one towards the right, so we need to save this information somewhere. Lets say every element of left moves to the right by **x**.
    * if first element of **left** is smaller than the first element of **right**, we can put that item in the sorted array, we know it has moved by **x** so we save that info as well.

### Code
```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]: 
        # stores the times by which a number moves to right
        # we only store this by the indices.
        indices = {} 
        # indices[1] = 2 means number in the input at index 1 
        # has moved by 2 places to the right         
        
        # we recreate the input but also save the original index
        # so it is not lost when we rearrage the list
        numsWithIndex = []
        for i in range(len(nums)):
            numsWithIndex.append([nums[i], i])
            indices[i] = 0
        
        # this method divides the input into 2 equal parts
        # and also applies the merging Logic to the parts
        def divideIntoLists(numsList):
            if len(numsList) <= 1:
                return numsList
            mid = len(numsList)//2
            return mergeLists([divideIntoLists(numsList[:mid]), divideIntoLists(numsList[mid:])])
        
        # important merging logic
        def mergeLists(twoLists):
            # break the input into left and right parts
            [left, right] = twoLists

            # the sorted list so far, based on input
            sortedList = []

            # this will save the info of how much to the right has 
            # the elements in the left array has moved
            rightCounter = 0

            while left or right:
                if right and not left:
                    # all info has been saved, we can just concat 
                    # what's left to the sortedList
                    return sortedList + right
                elif left and not right:
                    # means there were elements on the right array that 
                    # were smaller than the items of left array
                    # need to log the info into the indices dictionary
                    indices[left[0][1]] += rightCounter
                    sortedList.append(left.pop(0)) 
                elif left[0][0] > right[0][0]:
                    # since elements of the right array are greater, 
                    # elements of the left array will have to move by 1
                    rightCounter += 1
                    sortedList.append(right.pop(0))
                else:
                    indices[left[0][1]] += rightCounter
                    sortedList.append(left.pop(0))
            return sortedList
        
        divideIntoLists(numsWithIndex)
        
        # return the times, number at all indices moved to the right
        return [indices[i] for i in range(len(nums))]
```