## Question:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
```
Example:
--------
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## Solution:
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ret = ListNode(0)
        current = ret
        while l1 or l2 or carry:
            elem_l1 = l1 if l1 else ListNode(0)
            elem_l2 = l2 if l2 else ListNode(0)
            sum_elem = elem_l1.val + elem_l2.val + carry
            if sum_elem >= 10:
                current.next = ListNode(sum_elem % 10)
                carry = 1
            else:
                current.next = ListNode(sum_elem)
                carry = 0  
            current = current.next
            l1, l2 = elem_l1.next, elem_l2.next
        return ret.next
```
