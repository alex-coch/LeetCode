from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        nxt = None

        while cur:
            dummy = cur.next
            cur.next = nxt
            nxt = cur
            cur = dummy

            # dummy = cur.next
            # cur.next = nxt
            # nxt = cur
            # cur = dummy

        return nxt


l5 = ListNode(5)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

print(Solution().reverseList(head=l1).val)
# print(l5.next.val)