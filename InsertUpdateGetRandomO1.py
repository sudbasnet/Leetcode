'''
Implement the RandomizedSet class:

    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when 
        this method is called). Each element must have the same probability of being returned.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?
'''
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        """
        have a list and a dictionary ???
        pick random index from list ??
        
        dictionary will have the index for a number.
        if it is removed, there will be an index but no value in the array
        to remove something, find the object, replace it with the last element of the array then pop the array
        
        --- so simple !!!
        
        """
        self.validNums = []
        self.indexes = {}
        

    def insert(self, val: int) -> bool:           
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indexes:
            return False
        else:
            self.validNums.append(val)
            self.indexes[val] = len(self.validNums) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.indexes:
            if len(self.validNums) > 1:
                valIndex = self.indexes[val]
                self.validNums[-1], self.validNums[valIndex] = self.validNums[valIndex], self.validNums[-1]
                self.indexes[self.validNums[valIndex]] = valIndex
            del self.validNums[-1]
            del self.indexes[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randIndex = random.randint(0, len(self.validNums)-1)
        return self.validNums[randIndex]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()