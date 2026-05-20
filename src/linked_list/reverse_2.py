# Definition for singly-linked list.
from typing import Optional

from src.linked_list.support import prepare_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        cur = head
        prev = None
        while idx < left and cur:
            prev = cur
            cur = cur.next
            idx += 1

        dum = prev
        end = cur
        prev = None

        while idx <= right and cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            idx += 1

        end.next = cur
        if dum:
            dum.next = prev

        return prev if left == 1 else head





head = prepare_list([3, 5])
print_list(Solution().reverseBetween(head, 1, 2))

head = prepare_list([1,2,3,4,5])
print_list(Solution().reverseBetween(head, 2, 4))

head = prepare_list([5])
print_list(Solution().reverseBetween(head, 1, 1))