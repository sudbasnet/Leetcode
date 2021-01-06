'''
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:
----------
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
----------
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:
    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed is a permutation of popped.
    pushed and popped have distinct values.

'''

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        '''
        how about we replicate the process
        go from left to right in the pushed array and find the one 
        that matches with the first pop.
        In our example, we have 1,2,3,4 (this is the point where the first pop happens),
        since popped = [4, 5, ....]
        so 4 and 4 is validated,
        check the next item in popped, is it the same as the prev element of pushed?
        if no then move forward in pushed until the num is same as the num in popped.
        validate that, then move backwards in the pushed check if the next element in
        both match else move forward in pushed and find the next element in pushed that 
        matches with the popped. we stop when we have reached the popped array. If both
        have all elements satisfied??
        
        Is it a DP problem? does not look like it
        Is it a graph or tree traversal problem?? does not look like it
        Is it a two pointer problem?? yea, but in different arrays
        
        similar concept but better execution:
        create a stack, push into it from pushed array as long as you can,
        try popping each element, if it cant, then dont.
        '''
        
        stack = []
        iPush, iPop = 0, 0
        
        while iPush < len(pushed):
            stack.append(pushed[iPush])
            iPush += 1
            while stack and stack[-1] == popped[iPop]:
                stack.pop()
                iPop += 1

        if not stack:
            return True
        return False