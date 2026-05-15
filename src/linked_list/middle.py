from typing import Optional

from src.linked_list.support import prepare_list, ListNode, print_list


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

head = prepare_list([1,2,3,4,5,6])
print_list(Solution().middleNode(head))


