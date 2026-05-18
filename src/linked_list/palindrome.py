from typing import Optional

from src.linked_list.support import ListNode, prepare_list, print_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        idx = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            idx += 1

        prev = None
        cur = head
        while idx > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            idx -= 1

        if fast:
            slow = slow.next
        while slow and prev:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next

        return True


head = prepare_list([1,2,2,1])
# head = prepare_list([1,2])
head = prepare_list([1,0,1])
result = Solution().isPalindrome(head)

print(result)