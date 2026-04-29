from typing import Optional

def print_list(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        left = tmp
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return tmp.next



l2 = ListNode(2)
head = ListNode(1, l2)

print_list(Solution().removeNthFromEnd(head, 2))


