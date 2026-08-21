from typing import Optional

from src.linked_list.support import ListNode, prepare_list
from src.trees.support import TreeNode, print_bst


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut left part from middle
        prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root

head = prepare_list([-10,-3,0,5,9])
print_bst(Solution().sortedListToBST(head))