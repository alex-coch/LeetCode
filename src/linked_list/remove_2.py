# Definition for singly-linked list.
from typing import Optional

from src.linked_list.support import prepare_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:

                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next

            else:
                prev = prev.next

            curr = curr.next

        return dummy.next


head = prepare_list([2,3,3,4,4,5])
print_list(Solution().deleteDuplicates(head))

head = prepare_list([1,1,1,2,3])
print_list(Solution().deleteDuplicates(head))

head = prepare_list([1,1])
print_list(Solution().deleteDuplicates(head))