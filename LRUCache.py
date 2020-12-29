class DoublyLinkedList:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
    def __str__(self):
        return f"key: {self.key}, val: {self.val}"

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = DoublyLinkedList(), DoublyLinkedList()
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = collections.defaultdict(DoublyLinkedList)
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            current = self.cache[key]
            # in case the value has updated
            current.val = value
            # check if the key val is already the first in LL
            if self.head.next.key == key: 
                # do nothing
                return
            else:
                # adjust the prev and next obj
                current.prev.next = current.next
                current.next.prev = current.prev
        else:
            # create a new object since it doesn't exist
            current = DoublyLinkedList(key=key, val=value)
            if len(self.cache) == self.capacity:
                # remove the LL obj that's at the end on LL
                self.cache.pop(self.tail.prev.key)
                # adjust for the removal
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
        # put the current node at the front on the LL
        current.next = self.head.next
        current.prev = self.head
        self.head.next.prev =  current
        self.head.next = current 
        # add the current node into the cache dictionary
        self.cache[key] = current

        
    def get(self, key: int) -> int:
        if key in self.cache:
            # if exists in cache, put in the front
            self.put(key, self.cache[key].val)
            # return the value
            return self.cache[key].val
        else:
            return -1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

## SHORTEST VERSION
import collections

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
        else:
            if len(self.cache) == self.capacity: self.cache.popitem(last=False)
            self.cache[key] = Node(key, value)
        self.cache.move_to_end(key)             
            
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key].value
        return -1