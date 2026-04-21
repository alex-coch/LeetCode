# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

l1_3 = ListNode(4)
l1_2 = ListNode(2, l1_3)
l1_1 = ListNode(1, l1_2)

l2_3 = ListNode(4)
l2_2 = ListNode(3, l2_3)
l2_1 = ListNode(1, l2_2)

n_l = Solution().mergeTwoLists(l1_1, l2_1)

while n_l:
    print(n_l.val, end= " ")
    n_l = n_l.next