from typing import Optional

from src.linked_list.support import ListNode, prepare_list, print_list


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        idx = 0
        while fast and fast.next and idx < 10**4:
            slow = slow.next
            fast = fast.next.next
            idx += 1

            if id(fast) == id(slow):
                while id(head) != id(slow):
                    head = head.next
                    slow = slow.next
                return head

        return None


head = prepare_list([3,2,0,-4], 1)
head = prepare_list([1,2], pos = 0)
# head = prepare_list([1])
# head = prepare_list([1, 2])
# head = prepare_list([-1,-7,7,-4,19,6,-9,-5,-2,-5], 6)
result = Solution().detectCycle(head)
print(result.val)