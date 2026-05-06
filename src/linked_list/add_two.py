from typing import Optional

def print_list(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

def prepare_list(ml):
    new_head = ListNode(0)
    cur = new_head
    for val in ml:
        tmp = ListNode(val)
        cur.next = tmp
        cur = tmp
    return new_head.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        cur = tmp

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return tmp.next


# l3 = ListNode(3)
# l2 = ListNode(4, l3)
# head = ListNode(2, l2)
#
# l3_2 = ListNode(4)
# l2_2 = ListNode(6, l3_2)
# head_2 = ListNode(5, l2_2)

# l7 = ListNode(9)
# l6 = ListNode(9, l7)
# l5 = ListNode(9, l6)
# l4 = ListNode(9, l5)
# l3 = ListNode(9, l4)
# l2 = ListNode(9, l3)
# head = ListNode(9, l2)
#
# l4_2 = ListNode(9)
# l3_2 = ListNode(9, l4_2)
# l2_2 = ListNode(9, l3_2)
# head_2 = ListNode(9, l2_2)

# print_list(prepare_list([1, 2, 3]))

head = prepare_list([3, 7])
head_2 = prepare_list([9, 2])

print_list(Solution().addTwoNumbers(head, head_2))