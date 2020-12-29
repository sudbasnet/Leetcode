'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack  = []

    def push(self, x: int) -> None:
        if (self.minStack and x < self.minStack[-1][1]) or not self.minStack:
            self.minStack.append((x, x))
        else:
            self.minStack.append((x, self.minStack[-1][1]))

    def pop(self) -> None:
        if self.minStack:
            return self.minStack.pop()[0]
        return None

    def top(self) -> int:
        if self.minStack:
            return self.minStack[-1][0]
        return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1][1]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()