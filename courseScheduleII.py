class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        '''
        looks like a tree structure
         -> = 'depends on'
        a -> b -> c
               -> d -> e

        x -> None
        y -> None

        '''
        # make some vaiables that you can track
        # through the methods, and initialize them
        self.courseSequence = []
        self.dependencies = {}
        self.seen = {}
        for i in range(numCourses):
            self.dependencies[i] = []
            self.seen[i] = False

        for [node, dependsOn] in prerequisites:
            self.dependencies[node].append(dependsOn)

        def checkSchedule(start):
            stack = [start]
            while stack:
                current = stack[-1]
                while self.dependencies[current] and self.seen[self.dependencies[current][-1]]:
                    self.dependencies[current].pop()
                if self.dependencies[current]:
                    stack.append(self.dependencies[current].pop())
                else:
                    newNode = stack.pop()
                    self.courseSequence.append(newNode)
                    self.seen[newNode] = True

        for i in range(numCourses):
            if not self.seen[i]:
                checkSchedule(i)

        if len(self.courseSequence) == numCourses:
            return self.courseSequence
        return []
