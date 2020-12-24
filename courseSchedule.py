"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        to take course 0 must take course 1 [0,1]
        
        is it possible to finish all courses?
        do a topological sort, if all items are in the final sorted array, then you can return true
        """
#         if 1 is visited, then I can do 0
#         can I make it a parent - child relationship??
        
#         so 1 is the parent of 0
#         since we have the num of courses, 
#         we can start by checking each, 
        
#         or how many are dependent on 0??
#         those are 0's children

# first create a graph like object for each point
# if has no dependencies then its fine but it it has a dependency then it will be in 
        
        # initialization
        self.dependencies = {}
        for num in range(numCourses):
            self.dependencies[num] = []
            
        for prereq in prerequisites:
            self.dependencies[prereq[0]].append(prereq[1])
        
        print(self.dependencies)
        self.executionOrder = []
        self.hasCycle = False 
        
        def checkDependencies(courseNum):
            stack = [courseNum]
            while stack:
                current = stack[-1]
                # to check if there is a cycle, I need to check if the dependencies of the 
                # current element is already in the stack or not
                while self.dependencies[current] and self.dependencies[current][-1] in self.executionOrder:
                    self.dependencies[current].pop()

                if self.dependencies[current]:
                    newCourse = self.dependencies[current].pop()
                    if newCourse in stack:
                        self.hasCycle = True
                        return
                    stack.append(newCourse)
                else:
                    self.executionOrder.append(stack.pop())
            return
                    
        for i in range(numCourses):
            if i not in self.executionOrder:
                checkDependencies(i)
                
        # print(self.executionOrder)
        if len(self.executionOrder) == numCourses and not self.hasCycle:
            return True
        return False