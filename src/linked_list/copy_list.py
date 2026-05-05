from typing import Optional

def print_list(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy_hm = {None: None }

        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy_hm[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old_to_copy_hm[cur]
            copy.next = old_to_copy_hm[cur.next]
            copy.random = old_to_copy_hm[cur.random]
            cur = cur.next

        return old_to_copy_hm[head]


l2 = Node(2)
head = Node(1, l2)

print_list(Solution().copyRandomList(head))