# Definition for singly-linked list.
from typing import Optional

from src.linked_list.support import prepare_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dum_1 = ListNode(0, head)

        cur_2 = ListNode(0, None)
        dum_2 = ListNode(0, cur_2)
        prev_2 = dum_2

        cur = head
        prev = dum_1

        while cur:
            while cur and cur.val >= x:
                prev_2.next = cur
                prev_2 = prev_2.next
                cur = cur.next

            if cur:
                prev.next = cur
                prev = prev.next
                cur = cur.next

        prev_2.next = None
        prev.next = dum_2.next

        return dum_1.next

head = prepare_list([1,2])
print_list(Solution().partition(head, 2))

head = prepare_list([1,4,3,2,5,2])
print_list(Solution().partition(head, 3))

