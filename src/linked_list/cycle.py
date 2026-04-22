# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


