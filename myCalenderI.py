"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

"""

"""
I used a sorted LinkedList, but I could have used a list, and 
when I am searchin for the slot where I can insert the new event,
I could have used Binary search ? Not easy
"""


class Node:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        self.next = None


class MyCalendar:
    '''
    Maybe a linked list is a good idea ?? Yea, but I could optimize it a little

    '''

    def __init__(self):
        self.head = Node(float('-inf'), float('-inf'))

    def book(self, start: int, end: int) -> bool:
        event = Node(start, end)
        current = self.head
        while current:
            if current.end <= event.start and (not current.next or current.next.start >= event.end):
                event.next = current.next
                current.next = event
                return True
            current = current.next
        return False

# class Event:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

# class MyCalendar:
#     def __init__(self):
#         self.bookings = []

#     def book(self, start: int, end: int) -> bool:
#         s, e = 0, len(self.bookings) - 1
#         if not self.bookings:
#             self.bookings.append(Event(start, end))
#             return True
#         while s <= e:
#             mid = (s + e)//2
#             if self.bookings[mid].end <= start and (mid == len(self.bookings)-1 or self.bookings[mid+1].start >= end):
#                 self.bookings[:mid+1] + [Event(start, end)] + self.bookings[mid+1:]
#                 return True
#             if self.bookings[mid].end <= start:
#                 s = mid + 1
#             else:
#                 e = mid - 1
#         return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
