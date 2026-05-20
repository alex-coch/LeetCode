# Definition for singly-linked list.
from typing import Optional

from src.linked_list.support import prepare_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        idx = 0
        dum = ListNode(0, head)
        cur = head

        while cur:
            cur = cur.next
            idx += 1

        k %= idx

        if idx == 1 or k == 0:
            return head

        cur = dum.next
        prev = dum
        cnt = 0

        while cnt < idx - k:
            prev = cur
            cur = cur.next
            cnt += 1

        # print(cur.val)

        begin = cur
        prev.next = None

        while cur:
            prev = cur
            cur = cur.next

        # begin.next = None
        prev.next = dum.next
        dum.next = begin


        return dum.next

head = prepare_list([1, 2])
print_list(Solution().rotateRight(head, 2))

head = prepare_list([1, 2])
print_list(Solution().rotateRight(head, 0))

head = prepare_list([1])
print_list(Solution().rotateRight(head, 0))

head = prepare_list([0,1,2])
print_list(Solution().rotateRight(head, 4))

head = prepare_list([1,2,3,4,5])
print_list(Solution().rotateRight(head, 2))