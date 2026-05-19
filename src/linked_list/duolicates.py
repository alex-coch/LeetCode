# Definition for singly-linked list.
from typing import Optional

from src.linked_list.support import prepare_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        cur = head

        while True:
            cur = cur.next

            if cur is None or prev.val != cur.val:
                prev.next = cur
                prev = cur

            if cur is None:
                break

        return head


head = prepare_list([1,1,2,3,3])
# head = prepare_list([1, 1, 1])
print_list(Solution().deleteDuplicates(head))