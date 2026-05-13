from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = cur = ListNode(0)

        while any(lists):
            min_val = float("inf")
            for idx, node in enumerate(lists):
                if node and node.val <= min_val:
                    min_val = node.val
                    min_idx = idx
            cur.next = ListNode(min_val)
            cur = cur.next
            lists[min_idx] = lists[min_idx].next

        return head.next


head = prepare_list([1, 4, 5])
head_2 = prepare_list([1, 3, 4])
head_3 = prepare_list([2, 6])

print_list(Solution().mergeKLists([head, head_2, head_3]))

