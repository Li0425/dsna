from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Came up with the solution on my own
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = tail
            tail = curr
            curr = temp
            
        return tail
